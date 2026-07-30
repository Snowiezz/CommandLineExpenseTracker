import time
import database
def addExpense():
    category = input("What is the expense category?: ")
    amount = float(input("What is the expense amount?: £"))
    description = input("What is the expense description?: ")

    cleaned_amount = round(amount * 100) # turn to pence
    database.add_expense(category,cleaned_amount,description)
    print("Added to DB")
    
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
        time.sleep(3)



if __name__ == "__main__":
    main()

