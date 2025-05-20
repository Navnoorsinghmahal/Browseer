import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='shinkansen.proxy.rlwy.net',
            port=39462,
            database='railway',
            user='root',
            password='lqflxFEyccmTHvxPihysxkHsqaCRDpEC'
        )

        if connection.is_connected():
            print("Connected to Railway MySQL")
            return connection
    except Error as e:
        print(f"Connection failed: {e}")
        return None

def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE
        )
    """)
    print("Table 'users' ready")

def insert_data(cursor):
    query = "INSERT IGNORE INTO users (name, email) VALUES (%s, %s)"
    data = [
        ("Navnoor", "noormahal130505@gmail.com"),
        ("Raviit", "raviit.vij@gmail.com")
    ]
    cursor.executemany(query, data)
    print("Sample data inserted")

def read_data(cursor):
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("Data from 'users':")
    for row in rows:
        print(row)

def main():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()

        create_table(cursor)
        insert_data(cursor)
        conn.commit()
        read_data(cursor)

        cursor.close()
        conn.close()
        print("Connection closed")

if __name__ == "__main__":
    main()
