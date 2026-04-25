import os
import mysql.connector
from mysql.connector import Error


def get_db_connection():
    """Create and return a new MySQL connection using environment-safe defaults.

    This centralizes DB connection creation for the app and services.
    """
    try:
        host = os.getenv('DB_HOST', 'localhost')
        user = os.getenv('DB_USER', 'root')
        password = (
            os.getenv('DB_PASSWORD')
            or os.getenv('DB_PASS')
            or os.getenv('MYSQL_PWD')
            or os.getenv('MYSQL_ROOT_PASSWORD')
        )
        if not password:
            password = os.getenv('DB_FALLBACK_PASSWORD', 'root')
        database = os.getenv('DB_NAME', 'healthcare_crm')

        if not password:
            # Defensive check - should not happen due to fallback, but keep it explicit
            print('Warning: DB password is empty; please set DB_PASSWORD environment variable')

        conn_kwargs = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'autocommit': False,
        }
        return mysql.connector.connect(**conn_kwargs)
    except Error as e:
        print(f'MySQL connection failed: {e} (tried host={host} user={user} db={database})')
        raise
