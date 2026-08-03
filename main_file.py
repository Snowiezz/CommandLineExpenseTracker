import time
import database
import datetime
import matplotlib.pyplot as plt #graph
import matplotlib.dates as mdates # graph, converting x axis units

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

def checkBool(prompt):
    while True:
        result = input(prompt).strip().lower()
        if result == "y":
            return True
        elif result == "n":
            return False
        else:
            print("Please select Y (yes) or N (no)")






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
        print("Amount: £", amount/100)
        print("Description:", description)
        print("Date of expense: ",expense_date)

def deleteExpense():
    while True:
        expense_id = checkNumber("What is the ID for the expense? (press 0 to show current expenses): ")
        if expense_id == 0:
            showExpenses()
            continue
        else:
            confirmation = input("Are you sure? Y/N: ")
            if confirmation.lower() == "y":
                result = database.delete_expense(expense_id)
                if not result:
                    print("Expense not found, please check expense ID")
                    break
                print("Expense deleted.")

                break
            else:
                return

def updateExpense():
    while True:
        expense_id = checkNumber("What is the ID for the expense? (press 0 to show current expenses)")
        if expense_id == 0:
            showExpenses()
            continue
        else:
            print("What would you like to change?")
            print("1. Category")
            print("2. Amount")
            print("3. Expense Date")
            choice1 = int(input())
            if choice1 == 1:
                answer = database.update_expense("category",checkCategory(),expense_id)
                print(answer)


def showTotal(period):
    try:
        print("Spending by category: ")
        expenses = database.get_total(period)

        for category, amount in expenses:
            print(f"{category}: £{amount / 100:.2f}")

        total = sum(amount for _, amount in expenses)
        print(f"Total for {period}: £{total / 100:.2f}")
    except ValueError as error:
        print("Error: ", error)



def showExpenseGraph(period):
    try:
        results = database.get_expenses_over_time(period)
    except ValueError as error:
        print("Error: ", error)
        return
    if not results:
        print("There are no expenses")
        return
    dates = []
    amounts = []

    for expense_date, amount_pence in results:
        dates.append(datetime.date.fromisoformat(expense_date))
        amounts.append(amount_pence / 100)


    plt.figure(figsize=(9, 5))
    plt.bar(dates, amounts)
    today = datetime.date.today()
    if period == "week":
        plt.xlim(today - datetime.timedelta(days=6),today)
    elif period == "month":
        plt.xlim(today - datetime.timedelta(days=30),today)
    elif period == "all time" and len(dates) == 1:
        plt.xlim(
            dates[0] - datetime.timedelta(days=3),
            dates[0] + datetime.timedelta(days=3)
        )
    plt.title(f"Expenses over time — {period}")
    plt.xlabel("Date")
    plt.ylabel("Amount spent (£)")
    # change units to dd/mm
    axis = plt.gca()
    axis.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
    axis.xaxis.set_major_locator(mdates.DayLocator(interval=1)) # daily
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    return
def expenseAnalytics():
    while True:
        print("Welcome to your expense analytics")
        print("Select a time period:")
        print("-Week")
        print("-Month")
        print("-All time")
        print("press x to go back to the start")
        mode = input().lower()
        if mode in ["week","month","all time"]:
            showTotal(mode)
            if checkBool("Would you like to see the expenses graph? (Y or N):"):
                showExpenseGraph(mode)
            time.sleep(1)
        elif mode == "x":
            break
        else:
            print("Please choose one of the modes")
        



    
            




def main():
    database.create_database()
    while True:
        print("Welcome to the expenses tracker!")
        print("Please choose an option")
        print("1. Show expenses")
        print("2. Add a new expense")
        print("3. Delete an expense")
        print("4. Update an expense")
        print("5. Analytics")
        answer = checkNumber("Answer: ")

        if answer == 1:
            showExpenses()
        elif answer == 2:
            addExpense()
        elif answer ==3:
            deleteExpense()
        elif answer == 4:
            updateExpense()
        elif answer == 5:
            expenseAnalytics()
        time.sleep(2)



if __name__ == "__main__":
    main()

