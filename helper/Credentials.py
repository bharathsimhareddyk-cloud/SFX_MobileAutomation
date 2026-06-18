# SSH Tunnel Configuration
SSH_HOST = "gcprds.staging.db.shadowfax.in"
SSH_PORT = 22
SSH_USERNAME = "gcp-bastion-rds"
SSH_PKEY = r"D:\Installations\id_rsa"

STAGING_DB = {
    "connection_name": "staging_db",
    "host": "orc27gcp.staging.db.shadowfax.in",
    "port": 3306,
    "database": "frodo_staging",
    "user": "sf5994",
    "password": "wdehjga@1h4",
}

OTP_QUERY = "select otp from RMS_riderinfo WHERE allotted_phone=%s"
