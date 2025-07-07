import json
import sys
import argparse
from datetime import datetime
from prettytable import PrettyTable
import csv

# File paths for storing expenses and budgets
EXPENSE_FILE = "cart_list.json"
BUDGET_FILE = "monthly_budget.json"

def load_expenses():
    """
    Load the list of expenses from the JSON file.
    Returns an empty list if the file doesn't exist or is invalid.
    """
    try:
        with open(EXPENSE_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    """
    Save the list of expenses to the JSON file.
    Prints an error if saving fails.
    """
    try:
        with open(EXPENSE_FILE, 'w') as f:
            json.dump(expenses, f, indent=2)
    except Exception:
        print("❌ Error: Unable to save expenses")
    
def load_budgets():
    """
    Load the list of monthly budgets from the JSON file.
    Returns an empty list if the file doesn't exist or is invalid.
    """
    try:
        with open(BUDGET_FILE, 'r') as bud_f:
            return json.load(bud_f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_budget(budgets):
    """
    Save the list of budgets to the JSON file.
    Prints an error if saving fails.
    """
    try:
        with open(BUDGET_FILE,'w') as bud_file:
            json.dump(budgets,bud_file,indent=2)
    except Exception:
        print("❌ Error: Unable to save budget")
            
def create_id():
    """
    Generate a unique ID for a new expense.
    Returns the next available integer ID.
    """
    expenses = load_expenses()
    return max([expense['id'] for expense in expenses], default=0) + 1

def get_time_stamp():
    """
    Get the current date as a string in YYYY-MM-DD format.
    """
    return datetime.now().strftime("%Y-%m-%d")

def add_to_cart(desc, amount, category):
    """
    Add a new expense to the list after validating input and checking budget.
    """
    if not desc.strip():
        print("❌ Error: Description cannot be empty.")
        return
    if amount <= 0:
        print("❌ Error: Amount must be a positive number.")
        return

    expenses = load_expenses() 
            
    expense = {
        'id': create_id(),
        'date': get_time_stamp(),
        "description": desc.strip(),
        "amount": round(amount, 2),
        'category': category,
    }
    
    # Extract month from the date
    month = int(expense['date'].split('-')[1])   
    budgets = load_budgets()
    monthly_budget = 0
    
    # Get current total expenses for the month
    current_expense = get_filter_summary(month)
    
    # Find the budget for the current month
    for budget in budgets:
        if (budget['month'] == month):
            monthly_budget = budget['amount']
    
    # Check if adding this expense exceeds the monthly budget
    if (expense['amount'] + current_expense) > monthly_budget:
        print("❌ Error: You have exceeded your monthly budget.")
        return
    
    expenses.append(expense)
    save_expenses(expenses)
    print(f"✅ Expense added successfully (ID: {expense['id']})")

def remove_from_cart(id):
    """
    Remove an expense by its ID.
    Prints a message if the expense is not found.
    """
    expenses = load_expenses()
    found = False
    for expense in expenses:
        if expense['id'] == int(id):
            found = True
            expenses.remove(expense)
            save_expenses(expenses)
            print(f"🗑️ Expense deleted successfully (ID: {id})")
            break
    if not found:
        print(f"❌ Error: Expense with ID {id} not found.")

def set_budget(month, amount):
    """
    Set or update the budget for a specific month.
    Validates input and updates or adds the budget entry.
    """
    if amount <= 0:
        print("❌ Error: Amount must be a positive number.")
        return
    
    if int(month) < 1 or int(month) > 12:
        print("❌ Error: Month must be between 1 and 12.")
        return
    
    budgets = load_budgets()
    month = int(month)

    # Check if budget for this month already exists
    for budget in budgets:
        if budget['month'] == month:
            budget['amount'] = amount
            save_budget(budgets)
            print(f"✅ Budget updated successfully for month {month}")
            return

    # If not found, add a new entry
    budgets.append({
        "month": month,
        "amount": amount
    })
    save_budget(budgets)
    print(f"✅ Budget set successfully for month {month}")

def get_list():
    """
    Display all recorded expenses in a formatted table.
    """
    expenses = load_expenses()
    if not expenses:
        print("ℹ️ No expenses recorded yet.")
        return

    table = PrettyTable()
    table.field_names = ["ID", "Date", "Description", "Amount", "Category"]
    for expense in expenses:
        table.add_row([
            expense['id'],
            expense['date'],
            expense['description'],
            f"$ {float(expense['amount']):.2f}",
            expense['category']
        ], divider=True)
    print(table)

def create_expenses_csv(filename='Expenses_Summary.csv'):
    """
    Export all expenses to a CSV file.
    """
    expenses = load_expenses()

    if not expenses:
        print("ℹ️ No expenses recorded yet.")
        return

    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "date", "description", "amount", "category"])
            writer.writeheader()
            writer.writerows(expenses)
        print(f"✅ Expenses exported successfully to {filename}")
    except Exception as e:
        print(f"❌ Failed to export CSV: {e}")
    
def get_summary():
    """
    Print the total sum of all expenses.
    """
    expenses = load_expenses()
    total = sum(expense['amount'] for expense in expenses)
    print(f"📊 Total Expenses: $ {total:.2f}")

def get_filter_summary(month):
    """
    Calculate the total expenses for a specific month.
    Returns the sum as a float.
    """
    expenses = load_expenses()
    total = 0
    for expense in expenses:
        try:
            exp_month = int(expense['date'].split('-')[1])
            if exp_month == month:
                total += expense['amount']
        except (IndexError, ValueError):
            continue
    return total

def get_category_summary(category):
    """
    Print the total expenses for a specific category.
    """
    expenses = load_expenses()
    total = 0
    for expense in expenses:
        try:
            if expense['category'] == category:            
                total += expense['amount']
        except (IndexError, ValueError):
            continue
    print(f"📅 Total expenses of {category}: $ {total:.2f}")

def main():
    """
    Main entry point for the CLI application.
    Parses command-line arguments and calls the appropriate function.
    """
    if len(sys.argv) < 2:
        print("❗ Please provide a command: add, delete, list, summary")
        sys.exit()

    parser = argparse.ArgumentParser(description="🧾 Simple CLI Expense Tracker")
    subparsers = parser.add_subparsers(dest="command")

    # Add command parser
    add_parser = subparsers.add_parser("add", help="Add an expense")
    add_parser.add_argument('--description', help="Description of the item", required=True)
    add_parser.add_argument('--amount', help="Amount spent", type=float, required=True)
    add_parser.add_argument('--category', help="Tell which category the expense belong", default="None", required=False)

    # Delete command parser
    delete_parser = subparsers.add_parser("delete", help="Delete an expense by ID")
    delete_parser.add_argument('--id', type=int, required=True, help="Expense ID to delete")

    # List command parser
    subparsers.add_parser("list", help="List all recorded expenses")

    # Summary command parser
    summary_parser = subparsers.add_parser("summary", help="Get total expense summary")
    summary_parser.add_argument('--category', help="Get summary filtered by category")
    summary_parser.add_argument('--month', help="Get summary of a specific month", type=int, choices=range(1, 13))

    # Budget setting command parser
    budget_parser = subparsers.add_parser("budget", help="Set budget for a category")
    budget_parser.add_argument('--month', help="Set budget of a specific month", type=int, choices=range(1, 13), required=True)
    budget_parser.add_argument('--amount', help='set amount of the budget', type=float, required=True)
    
    # Export to CSV command parser
    export_parser = subparsers.add_parser("export", help="Export all expenses to CSV")
    export_parser.add_argument('--filename', help="Specify the output CSV filename", default="Expenses_Summary.csv")

    try:
        args = parser.parse_args()
        match args.command:
            case "add":
                add_to_cart(args.description, args.amount, args.category)
            case "delete":
                remove_from_cart(args.id)
            case "budget":
                set_budget(args.month, args.amount)
            case "list":
                get_list()
            case "export":
                create_expenses_csv(args.filename)
            case "summary":
                if args.month:
                    total = get_filter_summary(args.month)
                    month_name = datetime(1900, args.month, 1).strftime('%B')
                    print(f"📅 Total expenses for {month_name}: $ {total:.2f}")
                elif args.category:
                    get_category_summary(args.category)
                else:
                    get_summary()
            case _:
                print("❌ Invalid command. Use --help for usage info.")
    except Exception as e:
        print(f"🚨 An error occurred: {e}")

if __name__ == '__main__':
    main()
