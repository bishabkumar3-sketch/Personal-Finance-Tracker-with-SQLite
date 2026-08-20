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
