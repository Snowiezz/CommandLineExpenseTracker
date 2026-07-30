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
            return round(amount * 100)
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

def checkNumber(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number")






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
    for id, category, amount, description,expense_date in expenses:
        print()
        print("ID:", id)
        print("Category:", category)
        print("Amount:", amount)
        print("Description:", description)
        print("Date of expense: ",expense_date)

def deleteExpense():
    while True:
        expense_id = checkNumber("What is the ID for the expense? (press 0 to show current expenses): ")
        if expense_id == 0:
            showExpenses()
            continue
        result = database.delete_expense(expense_id)
        if not result:
            print("Expense not found, please check expense ID")
        else:
            print("Expense deleted.")
            break

def showTotal(period):
    try:
        total_pence = database.get_total(period)
        print(f"Total for {period}: £{total_pence / 100:.2f}")
    except ValueError as error:
        print("Error: ", error)

def expenseAnalytics():
    while True:
        print("Welcome to your expense analytics")
        print("Select a mode:")
        print("1. Week")
        print("2. Month")
        print("3. All time")
        mode = checkNumber("")
        if mode == 1:
            print("This Week")
            showTotal("week")
        elif mode == 2:
            print("Month")
            showTotal("month")
        elif mode == 3:
            print("All time")
            showTotal("all")
        else:
            print("Please choose one of the modes")
        



    
            




def main():
    database.create_database()
    while True:
        print("Welcome to the expenses tracker!")
        print("Please choose an option (1,2,3)")
        print("1. Show expenses")
        print("2. Add a new expense")
        print("3. Delete an expense")
        print("4. Expenses analytics")
        answer = checkNumber("Answer: ")

        if answer == 1:
            showExpenses()
        elif answer == 2:
            addExpense()
        elif answer ==3:
            deleteExpense()
        elif answer == 4:
            expenseAnalytics()
        time.sleep(2)



if __name__ == "__main__":
    main()

