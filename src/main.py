from import_data import load_transactions
from database import create_connection, view_transactions

transaction = view_transactions()

for transaction in transaction:
    print(transaction)

def main():
    file_path = "data/sample_statement.csv"

    transactions = load_transactions(file_path)

    print("Cleaned Transactions:")
    print(transactions)

    print("\nData Types:")
    print(transactions.dtypes)
    print(transactions)

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

if __name__ == "__main__":
    main()

