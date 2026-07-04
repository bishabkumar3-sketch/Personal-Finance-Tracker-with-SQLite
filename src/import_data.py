import pandas as pd


def load_transactions(file_path):
    """
    Reads the CSV file and returns a pandas DataFrame.
    """

    df = pd.read_csv(file_path)

    return df

