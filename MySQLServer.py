
import mysql.connector

def create_database():
    connection = None
    cursor = None

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
            cursor.execute("CREATE DATABASE IF NOT EXISTS `alx_book_store`")
            # Optional: safe habit for DDL
            # connection.commit()
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"MySQL error: {e}")
    
    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Ensure resources are closed safely
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
    create_database()
