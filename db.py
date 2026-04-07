import os
import mysql.connector
from mysql.connector import Error


def get_db_connection():
    """Create and return a new MySQL connection using environment-safe defaults.

    This centralizes DB connection creation for the app and services.
    """
    try:
        return mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', 'Amaan@123'),
            database=os.getenv('DB_NAME', 'healthcare_crm'),
            autocommit=False,
        )
    except Error:
        raise
