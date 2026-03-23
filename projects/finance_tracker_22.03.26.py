# PROJECT: Personal Finance Tracker
#
# Build a command-line app that lets you track income and expenses.
#
# Features to implement:
#   1. Log a transaction — ask for: type (income/expense), amount, category, description
#   2. View summary — total income, total expenses, net balance
#   3. Filter by category — show all transactions in a given category
#   4. Find the biggest expense
#   5. Quit
#
# Requirements:
#   - Use a list to store transactions (each transaction is a dictionary)
#   - Use a set to track unique categories
#   - Use functions — one per feature, at minimum
#   - Handle invalid input (e.g. non-numeric amount) with try/except
#   - Main loop should present a menu and call the right function
#
# Build this yourself. Come back when you have a feature working and I'll review it.
# Start with feature 1 — logging a transaction.

categories = set()
transactions = [
    {"Category": "bills", "Amount": 120.50, "Type": "expense", "Description": "Electric bill"},
    {"Category": "bills", "Amount": 45.00, "Type": "expense", "Description": "Water bill"},
    {"Category": "food", "Amount": 32.80, "Type": "expense", "Description": "Tesco shop"},
    {"Category": "food", "Amount": 15.00, "Type": "expense", "Description": "Takeaway"},
    {"Category": "income", "Amount": 1200.00, "Type": "income", "Description": "Salary"},
    {"Category": "entertainment", "Amount": 9.99, "Type": "expense", "Description": "Netflix"},
    {"Category": "entertainment", "Amount": 25.00, "Type": "expense", "Description": "Cinema"},
    {"Category": "transport", "Amount": 60.00, "Type": "expense", "Description": "Train pass"},
]


def main():
    while True: 
        user_type = input(f"\nWhat would you like to do? \n(1). Add a transaction\n(2). Summary \n(3). Search \n(4). Find the Largest Purchase\n(5). Quit\n").lower()
        if user_type in ("1", "transaction"):
            new_transaction()
        elif user_type in ("2", "summary"):
            summary()
        elif user_type in ("3", "search"):
            search_cat()
        elif user_type in ("4", "largest"):
            biggest_expense()
        elif user_type in ("5", "q", "quit"):
            break
        else:
            print("\nPlease enter a valid response.\n ")


def summary():
    positive = [(p["Category"],p["Amount"]) for p in transactions if p["Type"] == "income"]
    negative = [(p["Category"],p["Amount"]) for p in transactions if p["Type"] == "expense"]
    income_sum = sum([i["Amount"] for i in transactions if i["Type"] == "income"])
    expense_sum = sum([i["Amount"] for i in transactions if i["Type"] == "expense"])
    balance = income_sum-expense_sum
    print(f"Here is an overview of your account.\nBalance: {balance}")
    print(f"\nYou have the following incomes totalling {income_sum}: ")
    for i, e in positive:
        print(f"{i}: {e}")
    print(f"\nYou have the following expenses totalling {expense_sum}: ")
    for i, e in negative:
        print(f"{i}: {e}")
    input("\nPress enter to return to main menu\n")
    return


def search_cat():
    results = []
    user_search = input("What category would you like to search? ").lower()
    for x in transactions: 
        if x["Category"].lower() == user_search:
            results.append(x)
    if len(results) >= 1:
        for x in results:
            print(f"\n{x["Category"]}: {x["Amount"]} {x["Type"]}\n{x["Description"]}")
        input("\nPress enter to return to main menu\n")
        return
    else: 
        input("\nNo results found. Press enter to return to main menu\n")
        return

def biggest_expense():
    filtered = [a for a in transactions if a["Type"] == "expense"]
    biggest = max(filtered, key=lambda x: x["Amount"])
    print(f"{biggest["Category"]}: {biggest["Amount"]}")



def new_transaction():
    trans_type = ask_for_type()
    amount = ask_for_amount(trans_type)
    category = category_type()
    categories.add(category)
    description = trans_desc()
    transactions.append(create_dict(trans_type, amount, category, description))
    return amount


def ask_for_type():
    while True: 
        print("\nWhat type of transaction was this? \n")
        user_type = input("(1). Income (2). Expense \n").lower()
        if user_type in ("1", "income"):
            return "income"
        elif user_type in ("2", "expense"):
            return "expense"

def ask_for_amount(trans_type):
    while True:
        try: 
            if trans_type == "income":
                amount = float(input(f"\nHow much was the {trans_type}? \n"))
                return amount
            elif trans_type == "expense":
                amount = float(input(f"\nHow much was the {trans_type}? \n"))
                if amount < 0:
                    amount = -amount
                return amount
        except ValueError: 
            print("Please enter a number. ")

def category_type():
    while True:
        category = input("\nWhat category is this under? \n")
        if len(category) >=1:
            return category
        else:
            print("Please enter a category. ")

def trans_desc():
    while True:
        description = input("\nPlease set a description for this transaction? \n")
        if len(description) >=1:
            return description
        else:
            print("Please enter a description. ")

def create_dict(trans_type, amount, category, description):
    new_dict = {"Type": trans_type, "Amount": amount, "Category": category, "Description": description}
    print(f"\nYou had a {trans_type} totalling {amount} under the category: {category}\nDescription: {description}\n")
    return new_dict


main()

# TODO
# Implement full summary, for loop for transactions, dictionary comprehension. 
# Filter by category
# find biggest and smallest transactions
