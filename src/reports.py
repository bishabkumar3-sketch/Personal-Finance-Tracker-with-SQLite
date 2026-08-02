import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    conn = sqlite3.connect("finance_tracker.db")

    df = pd.read_sql_query("SELECT * FROM TRANSACTIONS", conn)

    conn.close

    return df


