from import_data import load_transactions
from database import *
from reports import (expense_by_category, income_vs_expense, monthly_expense)


def main():
    file_path = "data/sample_statement.csv"

    df = load_transactions(file_path)

    create_table()

    insert_transactions(df)

    print("===== All Transactions =====")
    for row in view_transactions():
        print(row)

    print("\n===== Expenses =====")
    for row in view_expenses():
        print(row)

    print("\n===== Income =====")
    for row in view_income():
        print(row)

    print("\n===== Summary =====")
    income = total_income()
    expense = total_expense()

    print("Income :", income)
    print("Expense:", expense)
    print("Balance:", income - expense)

    print("\nTransaction Count:", transaction_count())

    print("\nLargest Expense:")
    print(largest_expense())

if __name__ == "__main__":
    main()

expense_by_category()
income_vs_expense()
monthly_expense()
print("Reports generated and saved in the 'reports' directory.")