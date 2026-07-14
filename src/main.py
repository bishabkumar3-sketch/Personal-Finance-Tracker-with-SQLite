from import_data import load_transactions
from database import create_connection, view_transactions
from database import (
    view_transactions,
    view_expenses,
    view_income,
    total_income,
    total_expense,
    transaction_count,
    largest_expense
)

print("===== All Transactions =====")
transactions = view_transactions()
for transaction in transactions:
    print(transaction)

print("\n===== Expenses =====")
expenses = view_expenses()
for expense in expenses:
    print(expense)

print("\n===== Income =====")
income_transactions = view_income()
for income in income_transactions:
    print(income)

print("\n===== Summary =====")
income = total_income()
expense = total_expense()
balance = income - expense

print(f"Total Income  : {income}")
print(f"Total Expense : {expense}")
print(f"Balance       : {balance}")

print("\n===== Transaction Count =====")
count = transaction_count()
print(f"Total Transactions: {count}")

print("\n===== Largest Expense =====")
largest = largest_expense()

if largest:
    print(largest)
else:
    print("No expense found.")



def main():
    file_path = "data/sample_statement.csv"

    transactions = load_transactions(file_path)

    print("Cleaned Transactions:")
    print(transactions)

    print("\nData Types:")
    print(transactions.dtypes)
    print(transactions)


if __name__ == "__main__":
    main()

