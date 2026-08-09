import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    conn = sqlite3.connect("finance_tracker.db")

    df = pd.read_sql_query("SELECT * FROM TRANSACTIONS", conn)

    conn.close

    return df


def expense_by_category():
    
    df = load_data()
    expenses = df[df["type"] == "expense"]
    category_expenses = expenses.groupby("category")["amount"].sum()

    plt.figure(figsize=(10, 6))

    category_expenses.plot(kind = "bar", color = "skyblue")

    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("AMOUNT")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("reports/expense_by_category.png")

    plt.close()
    plt.show()


def income_vs_exense():
    df = load_data()

    summary = df.groupby("type")["amount"].sum()

    plt.figure(figsize=(8, 6))

    summary.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=["lightgreen", "salmon"])

    plt.title("Income vs Expense")
    plt.ylabel("")

    plt.savefig("reports/income_vs_expense.png")

    plt.close()

def monthly_expense():
    df = load_data()

    df["date "] = pd.to_datetime(df["date"])
    