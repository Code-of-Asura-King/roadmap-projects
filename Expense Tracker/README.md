
# 💸 Expense Tracker CLI

A simple and user-friendly command-line interface (CLI) application to track your expenses, set monthly budgets, categorize spending, and export your records to a CSV file.

---

## 📦 Features

- ✅ Add, delete, and list expenses
- 📊 View total expenses
- 🗃️ Filter summary by category or month
- 📆 Set a monthly budget and get alerts if you exceed it
- 📤 Export expenses to CSV for reports or backups

---

## 🛠️ Requirements

- Python 3.6+
- Modules:
  - `argparse`
  - `json`
  - `csv`
  - `prettytable`

Install missing dependencies with:
```bash
pip install prettytable
````

---

## 🚀 How to Use

### 📌 Add Expense

```bash
python Expense_tracker.py add --description "Lunch" --amount 150 --category Food
```

### ❌ Delete Expense

```bash
python Expense_tracker.py delete --id 3
```

### 📋 List All Expenses

```bash
python Expense_tracker.py list
```

### 📈 Summary

* All Expenses:

  ```bash
  python Expense_tracker.py summary
  ```

* By Month:

  ```bash
  python Expense_tracker.py summary --month 7
  ```

* By Category:

  ```bash
  python Expense_tracker.py summary --category Travel
  ```

### 💰 Set Monthly Budget

```bash
python Expense_tracker.py budget --month 7 --amount 5000
```

### 🧾 Export to CSV

```bash
python Expense_tracker.py export --filename July_Report.csv
```

---

## 📁 File Structure

| File                   | Description                       |
| ---------------------- | --------------------------------- |
| `Expense_tracker.py`   | Main CLI application script       |
| `cart_list.json`       | Stores all expense records        |
| `monthly_budget.json`  | Stores monthly budget information |
| `Expenses_Summary.csv` | Exported expense report           |

---

## 🔒 Data Validation & Error Handling

* Prevents negative or zero amounts
* Warns when monthly budget is exceeded
* Validates month ranges (1–12)
* Gracefully handles missing or corrupt JSON files

---

## ✨ Example

```bash
$ python Expense_tracker.py add --description "Bus Ticket" --amount 50 --category Transport
✅ Expense added successfully (ID: 1)

$ python Expense_tracker.py summary --month 7
📅 Total expenses for July: $ 50.00

$ python Expense_tracker.py export
✅ Expenses exported successfully to Expenses_Summary.csv
```

---

## 📌 Tips

* Use clear category names for better filtering (e.g., Food, Rent, Utilities)
* Run the `list` command often to monitor spending
* Set budgets early in the month to track effectively

---

## 📜 License

This project is for educational or personal use. Feel free to modify or extend it.

---

## 🙌 Acknowledgements

* Built with Python’s built-in modules and `prettytable` for clean tabular display.

