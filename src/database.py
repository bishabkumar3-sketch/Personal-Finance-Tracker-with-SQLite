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