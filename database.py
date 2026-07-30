import sqlite3 

DATABASE = "expenses.db"

def create_database():
    try:
        with sqlite3.connect(DATABASE) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY,
                    category TEXT NOT NULL,
                    amount_pence INTEGER NOT NULL
                )
            """)
    except sqlite3.error as error:
        print(f"Error: {error}")

def add_expense(category, amount, description):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute(
            """
            INSERT INTO expenses (category, amount, description)
            VALUES (?,?,?)
            """,
            (category,amount,description)
            )
        )