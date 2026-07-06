from typing import List, Dict, Any, Union

import mysql.connector
import psycopg2
import psycopg2.extras
import sshtunnel
from mysql.connector import Error

from helper.Credentials import SSH_HOST, SSH_PORT, SSH_USERNAME, SSH_PKEY, STAGING_DB, OTP_QUERY


class DBUtil:

    def __init__(self, dbms_type, host, database, user, password, port=3306):
        self.dbms_type  = dbms_type
        self.host       = host
        self.database   = database
        self.user       = user
        self.password   = password
        self.port       = port
        self._connection = None
        self._server     = None

    # ── Connection ────────────────────────────────────────────────────────────
    def get_connection(self):
        if self._connection is not None:
            return self._connection

        try:
            if self.dbms_type == 'mysql':
                self._connection = mysql.connector.connect(
                    host     = self.host,
                    port     = self.port,
                    database = self.database,
                    user     = self.user,
                    password = self.password
                )
                print('Successfully connected to MySQL database')

            elif self.dbms_type == 'postgres':
                self._server = sshtunnel.SSHTunnelForwarder(
                    (SSH_HOST, SSH_PORT),
                    ssh_username        = SSH_USERNAME,
                    ssh_pkey            = SSH_PKEY,
                    remote_bind_address = (self.host, 5432)
                )
                self._server.start()
                self._connection = psycopg2.connect(
                    host     = 'localhost',
                    port     = self._server.local_bind_port,
                    dbname   = self.database,
                    user     = self.user,
                    password = self.password
                )

            else:
                raise ValueError(f"Unsupported DBMS type: '{self.dbms_type}'")

        except Error as e:
            print(f"Connection error: {e}")

        return self._connection

    def disconnect(self):
        if self._connection:
            self._connection.commit()
            self._connection.close()
            self._connection = None

        if self._server:
            self._server.close()
            self._server = None

    # ── Query ─────────────────────────────────────────────────────────────────
    def execute_query(self, query: str, params: Union[tuple, Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        results = []
        try:
            connection = self.get_connection()

            if self.dbms_type == 'mysql':
                cursor_factory = {'dictionary': True}
            else:
                cursor_factory = {'cursor_factory': psycopg2.extras.RealDictCursor}

            with connection.cursor(**cursor_factory) as cursor:
                cursor.execute(query, params or ())
                results = cursor.fetchall()

            self.disconnect()

        except (Error, psycopg2.ProgrammingError) as e:
            print(f"Query error: {e}")

        return results


# ── Factories ─────────────────────────────────────────────────────────────────
def get_staging_db() -> DBUtil:
    return DBUtil(
        dbms_type = 'mysql',
        host      = STAGING_DB['host'],
        database  = STAGING_DB['database'],
        user      = STAGING_DB['user'],
        password  = STAGING_DB['password'],
        port      = STAGING_DB['port']
    )


def fetch_otp_for_mobile(mobile_number: str) -> str:
    db     = get_staging_db()
    result = db.execute_query(OTP_QUERY, (mobile_number,))
    if not result:
        raise RuntimeError(f"No OTP found for mobile number: {mobile_number}")
    return result[0]['otp']