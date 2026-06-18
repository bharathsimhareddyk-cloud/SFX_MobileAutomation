from typing import List, Dict, Any, Union

import mysql.connector
from mysql.connector import Error
import psycopg2
import psycopg2.extras
import sshtunnel

from helper.Credentials import SSH_HOST, SSH_PORT, SSH_USERNAME, SSH_PKEY, STAGING_DB, OTP_QUERY


class DBUtil:
    _instance = None
    _connection = None
    _server = None

    def __init__(self, dbms_type, host, database, user, password, port=3306):
        self.dbms_type = dbms_type
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    def get_connection(self):
        """
        Get or create a database connection.
        """
        if self._connection is None:
            try:
                if self.dbms_type == "mysql":
                    self._connection = mysql.connector.connect(
                        host=self.host,
                        port=self.port,
                        database=self.database,
                        user=self.user,
                        password=self.password
                    )
                elif self.dbms_type == "postgres":
                    self._server = sshtunnel.SSHTunnelForwarder((SSH_HOST, SSH_PORT),
                                                      ssh_username=SSH_USERNAME,
                                                      ssh_pkey=SSH_PKEY,
                                                      remote_bind_address=(self.host,5432))
                    self._server.start()
                    self._connection = psycopg2.connect(
                        host="localhost",
                        port=self._server.local_bind_port,
                        dbname=self.database,
                        user=self.user,
                        password=self.password
                    )
                else:
                    raise Exception(f"Unsupported dbms type {self.dbms_type}")
                if self.dbms_type == "mysql" and self._connection.is_connected():
                    print("Successfully connected to MySQL database")
            except Error as e:
                print(f"Error connecting to MySQL database: {e}")
        return self._connection

    def disconnect(self) -> None:
        """
        Close the database connection.
        """
        if self._connection:
            self._connection.commit()
            self._connection.close()
            self._connection = None

        if self._server:
            self._server.close()

    def execute_query(self, query: str, params: Union[tuple, Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Execute a SQL query and return the results.

        :param query: SQL query string
        :param params: Parameters for the query (optional)
        :return: List of dictionaries containing the query results
        """
        results = []
        try:
            connection = self.get_connection()
            if self.dbms_type == "mysql":
                with connection.cursor(dictionary=True) as cursor:
                    if params:
                        cursor.execute(query, params)
                    else:
                        cursor.execute(query)
                    results = cursor.fetchall()
                self.disconnect()
            else:
                with connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as cursor:
                    if params:
                        cursor.execute(query, params)
                    else:
                        cursor.execute(query)
                    results = cursor.fetchall()
                self.disconnect()
        except (Error,psycopg2.ProgrammingError)  as e:
            print(f"Error executing query: {e}")
        return results


def get_staging_db():
    return DBUtil(
        "mysql",
        STAGING_DB["host"],
        STAGING_DB["database"],
        STAGING_DB["user"],
        STAGING_DB["password"],
        STAGING_DB["port"],
    )


def fetch_otp_for_mobile(mobile_number):
    db = get_staging_db()
    result = db.execute_query(OTP_QUERY, (mobile_number,))
    if not result:
        raise RuntimeError(f"No OTP found for mobile number {mobile_number}")
    return result[0]["otp"]
