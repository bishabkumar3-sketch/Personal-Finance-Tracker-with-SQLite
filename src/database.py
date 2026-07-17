import sqlite3
db_name = "finance_tracker.db"

def create_connection():
    return sqlite3.connect(db_name)
 
def view_transactions():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")

    rows = cursor.fetchall()

    conn.close()

    return rows


def view_expenses():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM transactions
        WHERE type='Expense'
    """)

    rows = cursor.fetchall()

    conn.close()
    return rows

def view_income():
    conn = create_connection()
    cursor = conn.cursor()


    cursor.execute("""
        SELECT *
        FROM transactions
        WHERE type='Income'
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def total_income():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(amount)
        FROM transactions
        WHERE type='Income'
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total

def total_expense():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(amount)
        FROM transactions
        WHERE type='Expense'
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total

def transaction_count():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM transactions
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count

def largest_expense():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM transactions
        WHERE type='Expense'
        ORDER BY amount DESC
        LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()

    return row


def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            description TEXT,
            amount REAL,
            type TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_transactions(df):
    conn = create_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO transactions
            (date, description, amount, type)
            VALUES (?, ?, ?, ?)
        """, (
            row["date"],
            row["description"],
            row["amount"],
            row["type"]
        ))

    conn.commit()
    conn.close()