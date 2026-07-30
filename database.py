import sqlite3 

DATABASE = "expenses.db"

def create_database():
    try:
        with sqlite3.connect(DATABASE) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY,
                    category TEXT NOT NULL,
                    amount_pence INTEGER NOT NULL,
                    description TEXT,
                    expense_date TEXT NOT NULL,
                    expense_time TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """)
    except sqlite3.Error as error:
        print("Error:",error)

def add_expense(category, amount, description,expense_date):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute(
            """
            INSERT INTO expenses (category, amount_pence, description,expense_date)
            VALUES (?,?,?,?)
            """,
            (category,amount,description,expense_date)
            )
def get_expenses():
    with sqlite3.connect(DATABASE) as conn:
        return conn.execute(
            """
            SELECT * FROM expenses

            """
        ).fetchall()

def delete_expense(expense_id):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.execute(
                "DELETE FROM expenses where id=?",
                (expense_id,)
            )
            return cursor.rowcount > 0
    except sqlite3.Error as error:
        print("Error: ",error)
        return False