from import_data import load_transactions


def main():
    file_path = "data/sample_statement.csv"

    transactions = load_transactions(file_path)

    print("Cleaned Transactions:")
    print(transactions)

    print("\nData Types:")
    print(transactions.dtypes)


if __name__ == "__main__":
    main()