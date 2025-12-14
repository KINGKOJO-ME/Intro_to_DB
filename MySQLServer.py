import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (update host, user, password as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # replace with your MySQL username
            password="password" # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if not exists (no SELECT or SHOW used)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"MySQL error: {e}")
    
    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Ensure connection is closed
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()