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

def monthly_summary(month,year):

    df = load_data()

    df["date"] = pd.to_datetime(df["date"])

    monthly = df[(df["date"].dt.month == month) & (df["date"].dt.year == year)]

    income = monthly[monthly["type"] == "income"]["amount"].sum()

    expenses = monthly[monthly["type"] == "expense"]["amount"].sum()

    balance = income - expenses

    return monthly, income, expenses, balance

def monthly_top_category(month, year):

    monthly, _, _, _ = monthly_summary(month, year)

    expenses = monthly[monthly["type"] == "expense"]

    if expenses.empty:
        return None, 0
    
    category_total = expenses.groupby("category")["amount"].sum()

    category_total = category_total.idmax(), category_total.max()

    return category_total

def generate_monthly_report(month, year):

    monthly, income, expenses, balance = monthly_summary(month, year)

    category, category_amount = monthly_top_category(month, year)

    print(f"\n===== Monthly Financial Summary for {month}/{year} =====")

    print(f"month : {year}-{month:02d}")
    print(f"monthly Income : ₹{income:.2f}")
    print(f"monthly Expenses : ₹{expenses:.2f}")
    print(f"monthly Balance : ₹{balance:.2f}")

    if category is not None:
        print(f"highest spending category: {category} ({category_amount:.2f})")
    else:
        print("No expenses recorded for this month.")


    print("===============================================")