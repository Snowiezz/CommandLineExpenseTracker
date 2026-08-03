from expenses import checkNumber
import database
import datetime
def checkBudget():
    while True:
        try:
            amount = float(input("What would you like your budget to be?: £"))

            if amount <= 0:
                print("Amount must be greater than zero")
                continue
            return round(amount * 100)
        except ValueError:
            print("Please enter a valid amount")
def updateBudget():
    current_month = datetime.date.today().strftime("%Y-%m")
    budget = database.get_budget(current_month)
    if not budget:
        print("You don't have a budget this month")
        if database.set_budget(current_month,checkBudget()):
            print("Budget set")
    else:
        print("youve gotta budget")
def budgetsmain():
    database.create_database()
    while True:
        print()
        print("Welcome to the budget monitor!")
        print("1. Set/update your budget")
        print("2. Check budget allowance")
        answer = checkNumber("Answer: ")
        if answer == 1:
            updateBudget()

        
    