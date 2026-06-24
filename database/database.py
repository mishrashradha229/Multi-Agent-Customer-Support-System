import sqlite3

DB_NAME = "database/tickets.db"


def get_connection():
    """
    Create SQLite connection.
    """
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tickets (

            ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,

            customer TEXT,

            query TEXT,

            category TEXT,

            priority TEXT,

            status TEXT,

            resolution TEXT,

            language TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    initialize_database()
    print("Database Created Successfully")