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
def get_expenses(column,order):
    with sqlite3.connect(DATABASE) as conn:
        return conn.execute(
            f"""
            SELECT id,category,amount_pence,description,expense_date FROM expenses
            ORDER BY {column} {order}
            """
        ).fetchall()

def get_total(period):
    queries = {
        "week": """
            SELECT category, SUM(amount_pence)
            FROM expenses
            WHERE expense_date >= date('now', 'localtime', '-6 days')
            GROUP BY category
            ORDER BY SUM(amount_pence) DESC
        """,
        "month": """
            SELECT category, SUM(amount_pence)
            FROM expenses
            WHERE expense_date >= date('now', 'localtime', '-1 month')
            GROUP BY category
            ORDER BY SUM(amount_pence) DESC   
        """,
        "all time": """
            SELECT category, SUM(amount_pence)
            FROM expenses
            GROUP BY category
            ORDER BY SUM(amount_pence) DESC
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


def update_expense(column, change,expense_id):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.execute(
            f"""
            UPDATE expenses
            SET {column} = ?
            WHERE id=?
            """,
            (change,expense_id,))
            return cursor.rowcount > 0
    except sqlite3.Error as error:
        print("Error: ",error)
        return False