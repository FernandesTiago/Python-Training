# learning SQL

import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).parent / "employees.db"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        salary INTEGER
    )
""")
# cursor.execute("INSERT INTO employees (name, salary) VALUES (?, ?)", ("Tiago", 2500))
# cursor.execute("INSERT INTO employees (name, salary) VALUES (?,?)", ("Juliana", 3000))

# cursor.execute("UPDATE employees SET salary = 5000 WHERE id = 1")

# cursor.execute("DELETE FROM employees WHERE id = 1")

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

for item in rows:
    print(f"ID: {item[0]} | Name: {item[1]} | Salary: {item[2]}")


connection.commit()
connection.close()
