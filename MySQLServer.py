import mysql.connector

def create_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password"
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"MySQL error: {e}")

    finally:
        try:
            cursor.close()
            connection.close()
        except Exception:
            pass

if __name__ == "__main__":
    create_database()
