import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

database_name = os.environ.get('DB_DATABASE')
host = os.environ.get('DB_HOST')
user = os.environ.get('DB_USERNAME')
password = os.environ.get('DB_PASSWORD')

if not all([host, user, password]):
    raise ValueError("Missing one or more environment variables for database connection.")

try:
    connection = mysql.connector.connect(
        host = host,
        user = user,
        passwd = password
    )

    cursor = connection.cursor()

    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')

    print(f"Database '{database_name}' created successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
