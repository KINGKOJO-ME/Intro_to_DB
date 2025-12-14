
#!/usr/bin/env python3
"""
MySQLServer.py
Creates the database 'alx_book_store' on a MySQL server.

Requirements:
- Do not use SELECT or SHOW statements.
- Print success message when created.
- Print error message if connection/execution fails.
- Properly open and close the DB resources.
"""

import mysql.connector
from mysql.connector import Error


def create_database(host: str, user: str, password: str, port: int = 3306, db_name: str = "alx_book_store") -> None:
    """
    Connects to the MySQL server and creates the database if it doesn't exist.

    Args:
        host (str): MySQL server hostname or IP (e.g., 'localhost').
        user (str): MySQL username (e.g., 'root').
        password (str): MySQL password.
        port (int): MySQL port (default 3306).
        db_name (str): Database name to create (default 'alx_book_store').
    """
    connection = None
    cursor = None

    try:
        # Open a connection to the MySQL server (no specific DB yet)
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port
        )

        # Proceed only if connection succeeded
        if connection.is_connected():
            cursor = connection.cursor()

            # Create database safely without SELECT/SHOW
            create_db_sql = f"CREATE DATABASE IF NOT EXISTS `{db_name}`"

            # Execute the statement
            cursor.execute(create_db_sql)

            # Commit (safe habit for DDL)
            connection.commit()

            # Required success message
            print(f"Database '{db_name}' created successfully!")

    except Error as e:
        # Friendly error messages
        print("Error: Failed to connect to the MySQL server or execute the statement.")
        print(f"Details: {e}")

    finally:
        # Always close cursor and connection
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass

        if connection is not None and connection.is_connected():
            try:
                connection.close()
            except Exception:
                pass


if __name__ == "__main__":
    # === EDIT THESE TO MATCH YOUR SETUP ===
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "your_password_here"  # <-- replace with your password
    MYSQL_PORT = 3306

    # Create the database
    create_database(
        host=MYSQL_HOST,
        user        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        port=MYSQL_PORT,
        db_name="alx_book_store"
