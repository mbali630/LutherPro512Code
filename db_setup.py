import sqlite3
from config import DB_PATH

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create Books table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        isbn TEXT UNIQUE NOT NULL,
        title TEXT NOT NULL,
        author TEXT,
        publisher TEXT,
        publication_year INTEGER,
        category TEXT,
        description TEXT,
        cover_image_url TEXT,
        page_count INTEGER,
        language TEXT,
        total_copies INTEGER,
        available_copies INTEGER,
        shelf_location TEXT
    )
    """)

    # Create Members table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Members (
        member_id INTEGER PRIMARY KEY AUTOINCREMENT,
        membership_number TEXT UNIQUE NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        address TEXT,
        join_date TEXT,
        membership_type TEXT,
        status TEXT
    )
    """)

    # Create Transactions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER,
        book_id INTEGER,
        issue_date TEXT,
        due_date TEXT,
        return_date TEXT,
        fine_amount REAL DEFAULT 0,
        status TEXT,
        FOREIGN KEY(member_id) REFERENCES Members(member_id),
        FOREIGN KEY(book_id) REFERENCES Books(book_id)
    )
    """)

    conn.commit()
    conn.close()
    print("✅ Database tables created successfully!")

if __name__ == "__main__":
    create_tables()