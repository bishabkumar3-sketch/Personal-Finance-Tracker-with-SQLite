import sqlite3
import pandas as pd 

def load_data():
    conn = sqlite3.connect('finance.db')

    df = pd.read_sql_query("SELECT * FROM transactions", conn)

    conn.close()
    return df

