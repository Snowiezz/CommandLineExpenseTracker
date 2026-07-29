import time
def addExpense(expenses):
    category = input("What is the expense category?: ")
    amount = float(input("What is the expense amount?: £"))
    desc = input("What is the expense description?: ")
    expenses.append({
        "Category": category,
        "Amount": amount,
        "Description": desc
    })
def showExpenses(expenses):
    for expense in expenses:
        print()
        for key,value in expense.items():
            print(key,":",value)
        print()
    
            




def main():
    expenses = []
    while True:
        print("Welcome to the expenses tracker!")
        print("Please choose an option (1,2,3)")
        print("1. Show expenses")
        print("2. Add a new expense")
        print("3. Delete an expense")
        answer = int(input("Answer: "))

        if answer == 1:
            showExpenses(expenses)
        elif answer == 2:
            addExpense(expenses)
        time.sleep(1)



if __name__ == "__main__":
    main()

