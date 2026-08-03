from expenses import expensesmain,checkNumber
from budgets import budgetsmain

def start():
    while True:
        print()
        print("Welcome to the expenses tracker!")
        print("Choose a function")
        print("1. Manage your budget")
        print("2. Manage your expenses")
        answer = checkNumber("Answer: ")
        if answer == 1:
            budgetsmain()
        elif answer == 2:
            expensesmain()

if __name__ == "__main__":
    start()

