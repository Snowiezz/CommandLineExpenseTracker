import time
import sqlite3
import database
def addExpense():
    category = input("What is the expense category?: ")
    amount = float(input("What is the expense amount?: £"))
    description = input("What is the expense description?: ")

    cleaned_amount = round(amount * 100) # turn to pence
    database.add_expense(category,cleaned_amount,description)
    print("Added to DB")
    
def showExpenses(expenses):
    for expense in expenses:
        print()
        for key,value in expense.items():
            print(key,":",value)
        print()
    
            




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
        time.sleep(1)



if __name__ == "__main__":
    main()

