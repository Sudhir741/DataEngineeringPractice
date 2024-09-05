# Expense class
class Expense:
    def __init__(self, id, date, category, description, amount):
        self.id = id
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
    def __str__(self):
        return f"Expense {self.id}: {self.date} - {self.category} - {self.description} - {self.amount}"
# List to store expenses
expenses = []
# Functions to manipulate expenses
def add_expense(id, date, category, description, amount):
    expenses.append(Expense(id, date, category, description, amount))
def update_expense(id, date, category, description, amount):
    for expense in expenses:
        if expense.id == id:
            expense.date = date
            expense.category = category
            expense.description = description
            expense.amount = amount
            break
def delete_expense(id):
    for expense in expenses:
        if expense.id == id:
            expenses.remove(expense)
            break
def display_expenses():
    for expense in expenses:
        print(expense)
# User Auth
users = {"admin": "password", "user1": "password1", "user2": "password2"}
def authenticate_user(username, password):
    if username in users and users[username] == password:
        return True
    else:
        return False
#Summary
def categorize_expenses():
    categories = {}
    for expense in expenses:
        if expense.category not in categories:
            categories[expense.category] = 0
        categories[expense.category] += expense.amount
    return categories
def summarize_expenses():
    total = 0
    for expense in expenses:
        total += expense.amount
    return total

def cli():
    if authenticate_user(input("Username: "), input("Password: ")):
        while True:
            print("Menu:")
            print("1. Add expense")
            print("2. Update expense")
            print("3. Delete expense")
            print("4. Display expenses")
            print("5. Generate summary report")
            print("6. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                id = int(input("Expense ID: "))
                date = input("Date: ")
                category = input("Category: ")
                description = input("Description: ")
                amount = float(input("Amount: "))
                add_expense(id, date, category, description, amount)
            elif choice == "2":
                id = int(input("Expense ID: "))
                date = input("New date: ")
                category = input("New category: ")
                description = input("New description: ")
                amount = float(input("New amount: "))
                update_expense(id, date, category, description, amount)
            elif choice == "3":
                id = int(input("Expense ID: "))
                delete_expense(id)
            elif choice == "4":
                display_expenses()
            elif choice == "5":
                categories = categorize_expenses()
                for category, amount in categories.items():
                    print(f"Category: {category}, Total: {amount}")
                print(f"Total expenses: {summarize_expenses()}")
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")
# Run the program
cli()
