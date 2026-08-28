import sqlite3
import pandas as pd 

def load_data():
    conn = sqlite3.connect('finance.db')

    df = pd.read_sql_query("SELECT * FROM transactions", conn)

    conn.close()
    return df


def financial_summary():
    df = load_data()
    income = df[df["type"] == "income"]["amount"].sum()
    expenses = df[df["type"] == "expense"]["amount"].sum()

    balance = income - expenses

    return income, expenses, balance

def highest_spending_category():

    df = load_data()

    expenses = df[df["type"] == "expense"]

    category_total = expenses.groupby("category")["amount"].sum()
    
    return category_total.idxmax(), category_total.max()


def largest_expense():

    df = load_data()

    expenses = df[df["type"] == "expense"]

    largest = expenses.loc[expenses["amount"].idxmax()]

    return largest

def average_expense():

    df = load_data()

    expenses = df[df["type"] == "expense"]

    return expenses["amount"].mean()

def generate_summary():

    income , expenses, balance = financial_summary()

    category, category_amount = highest_spending_category()

    largest = largest_expense()
    avg_expense = average_expense()

    print("\n===== Financial Summary =====")

    print(f"Total Income : ₹{income:.2f}")
    print(f"Total Expenses : ₹{expenses:.2f}")
    print(f"Balance : ₹{balance:.2f}")

    print("\n---------SPENDING INSIGHT-----------")

    print(
        f"highest category: {category}"
        f"({category_amount:.2f})"
    )

    print(
        f"largest expense: {largest["description"]}"
        f"({largest["amount"]:.2f})"
    )

    print(f"average expense: ₹{avg_expense:.2f}")

    print("\n=====================================")