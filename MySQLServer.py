#imorts 
import mysql.connector
from mysql.connector import Error

def main ():
    config = {
        host: 'localhost',
        user: 'root',
        port: 3306,
        password: 'password'
    }

    connection = None

    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Connected to MySQL server successfully!")

    except Error as err:
        print(f"Error: Failed to connect to MySQL server. Details: {err}")

    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()