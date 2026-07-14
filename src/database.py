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