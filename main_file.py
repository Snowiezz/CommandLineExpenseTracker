import time
import database
import datetime

CATEGORIES = ["Food","Travel","Bills","Entertainment","Shopping","Miscellaneous"]

def checkAmount():
    while True:
        try:
            amount = float(input("What is the expense amount?: £"))

            if amount <= 0:
                print("Amount must be greater than zero")
                continue
            return (amount*100)
        except ValueError:
            print("Please enter a valid amount")
def checkCategory():
    while True:
        categoryanswer = input("What is the expense category? (press x for list of categories): ").strip()
        if categoryanswer.lower() == "x":
            print("List of categories:")
            for category in CATEGORIES:
                time.sleep(0.3)
                print(category)
            continue
        for category in CATEGORIES:
            if categoryanswer.lower() == category.lower():
                return category
        print("Please select a valid category")

def checkExpenseDate():
    while True:
        answer = input("When was this expense? (DD/MM/YY or press ENTER for today)").strip()

        if answer == "":
            return datetime.date.today().isoformat()
        try:
            expense_date = datetime.datetime.strptime(answer, "%d/%m/%y").date()

            if expense_date > datetime.date.today():
                print("The expense date cannot be in the future.")
                continue
            return expense_date.isoformat()
        except ValueError:
            print("Please use the DD/MM/YY format")






def addExpense():
    category = checkCategory()
    amount = checkAmount()
    description = input("What is the expense description?: ")
    expense_date = checkExpenseDate()

    database.add_expense(category,amount,description,expense_date)
    print("Added to the database.")
    
def showExpenses():
    expenses = database.get_expenses()

    if not expenses:
        print("You have no expenses.")
        return 
    for id, category, amount, description in expenses:
        print()
        print("ID:", id)
        print("Category:", category)
        print("Amount:", amount)
        print("Description:", description)

def deleteExpense():
    while True:
        expense_id = int(input("What is the ID for the expense? (press 0 to show current expenses): "))
        if expense_id == 0:
            showExpenses()
            continue
        result = database.delete_expense(expense_id)
        if not result:
            print("Expense not found, please check expense ID")
        else:
            print("Expense deleted.")
            break




    
            




def main():
    database.create_database()
    while True:
        print("Welcome to the expenses tracker!")
        print("Please choose an option (1,2,3)")
        print("1. Show expenses")
        print("2. Add a new expense")
        print("3. Delete an expense")
        answer = int(input("Answer: "))

        if answer == 1:
            showExpenses()
        elif answer == 2:
            addExpense()
        elif answer ==3:
            deleteExpense()
        time.sleep(2)



if __name__ == "__main__":
    main()

