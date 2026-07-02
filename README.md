# 💰 Personal Finance Tracker with SQLite

A Python-based **Personal Finance Tracker** that imports bank statement CSV files, stores transactions in a SQLite database, analyzes spending patterns using SQL, and generates insightful reports with data visualizations.

This project demonstrates practical skills in **Python, SQL, SQLite, Pandas, and Matplotlib** by building an end-to-end data analysis application.

---

## 🚀 Features

* 📂 Import bank statement CSV files
* 🧹 Clean and preprocess transaction data
* 🗄️ Store transactions in a SQLite database
* 🔍 Query financial data using SQL
* 📊 Analyze monthly income and expenses
* 🥧 Visualize spending by category with charts
* 📈 Generate monthly financial reports
* 💾 Export reports for future reference

---

## 🛠️ Tech Stack

* Python 3
* SQLite
* Pandas
* Matplotlib
* SQL

---

## 📁 Project Structure

```text
finance-tracker/
│
├── data/
│   └── bank_statement.csv
│
├── database/
│   └── finance.db
│
├── reports/
│
├── charts/
│
├── src/
│   ├── import_csv.py
│   ├── database.py
│   ├── analysis.py
│   ├── visualization.py
│   └── report.py
│
├── requirements.txt
└── README.md
```

---

## 📊 Database Schema

### transactions

| Column      | Type    | Description             |
| ----------- | ------- | ----------------------- |
| id          | INTEGER | Primary Key             |
| date        | TEXT    | Transaction Date        |
| description | TEXT    | Transaction Description |
| category    | TEXT    | Spending Category       |
| amount      | REAL    | Transaction Amount      |

---

## 📈 Example Analysis

The project can generate insights such as:

* Total Income
* Total Expenses
* Monthly Spending
* Monthly Savings
* Highest Expense
* Highest Income
* Spending by Category
* Transaction History

---

## 📷 Sample Visualizations

* Pie Chart for Category-wise Spending
* Monthly Expense Bar Chart
* Savings Trend Line Chart

> Add screenshots of your charts in this section after running the project.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/personal-finance-tracker.git
```

Navigate to the project directory:

```bash
cd personal-finance-tracker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python src/main.py
```

---

## 📂 Sample CSV Format

```csv
Date,Description,Amount
2026-01-01,Salary,50000
2026-01-02,Amazon,-1200
2026-01-03,Swiggy,-350
2026-01-05,Electricity Bill,-1800
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Reading and processing CSV files with Pandas
* Working with SQLite databases
* Writing SQL queries for data analysis
* Data cleaning and preprocessing
* Creating visualizations with Matplotlib
* Building a complete data analysis workflow

---

## 🔮 Future Improvements

* Budget tracking
* Expense category prediction using Machine Learning
* Interactive dashboard with Streamlit
* PDF report generation
* Multi-user support
* Search and filter transactions
* Email monthly reports

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork this repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
