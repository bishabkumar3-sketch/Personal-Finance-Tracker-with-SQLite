import pandas as pd


def load_transactions(file_path):
    """
    Reads the CSV file and returns a pandas DataFrame.
    """

    df = pd.read_csv(file_path)

    # Remove rows with missing valuesadd clean 
    df.dropna(inplace=True)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Convert the Date column to datetime
    df["date"] = pd.to_datetime(df["date"])
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")
    return df

