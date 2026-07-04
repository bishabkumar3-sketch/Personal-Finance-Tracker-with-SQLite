from import_data import load_transactions


def main():
    file_path = "data/sample_statement.csv"

    transactions = load_transactions(file_path)

    print(transactions)


if __name__ == "__main__":
    main()