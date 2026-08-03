import sqlite3 

DATABASE = "expenses.db"

def create_database():
    try:
        with sqlite3.connect(DATABASE) as conn:
            query = """
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY,
                    category TEXT NOT NULL,
                    amount_pence INTEGER NOT NULL,
                    description TEXT,
                    expense_date TEXT NOT NULL,
                    time_created TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            conn.execute(query)
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
            SELECT id,category,amount_pence,description,expense_date FROM expenses

            """
        ).fetchall()

def get_total(period):
    queries = {
        "week": """
            SELECT amount_pence,category
            FROM expenses
            WHERE expense_date >= date('now', 'localtime', '-7 days')
        """,
        "month": """
            SELECT amount_pence,category
            FROM expenses
            WHERE expense_date >= date('now', 'localtime', '-1 month')
        """,
        "all time": """
            SELECT amount_pence,category
            FROM expenses
        """
    }


    with sqlite3.connect(DATABASE) as connection:
        result = connection.execute(queries[period]).fetchall()
        return result

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
def get_expenses_over_time(period):
    filters = {
        "week": "WHERE expense_date >= date('now', 'localtime', '-6 days')",
        "month": "WHERE expense_date >= date('now', 'localtime', '-1 month')",
        "all time": ""
    }
    query = f"""
        SELECT expense_date, SUM(amount_pence)
        FROM expenses
        {filters[period]}
        GROUP BY expense_date
        ORDER BY expense_date
    """
    with sqlite3.connect(DATABASE) as conn:
        return conn.execute(query).fetchall()