# Create a terminal menu system with the options:

import sqlite3

# --------- DATABASE STRUCTURE ---------

class Database:

    def __init__(self):
        self.connection = sqlite3.connect("EmployeeMenu.db")
        self.cursor = self.connection.cursor()
        self.connection.execute("""
        CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        salary INTEGER
    )""")

    def read(self):
        self.cursor.execute("SELECT * FROM employees")
        return self.cursor.fetchall()

    def find_by_id(self, searched_id):
        self.cursor.execute("SELECT * FROM employees WHERE id = ?", (searched_id,))
        return self.cursor.fetchone()

    def save(self, new_name, new_salary):
        self.cursor.execute("INSERT INTO employees (name, salary) VALUES (?,?)", (new_name, new_salary))
        self.connection.commit()

    def update_name(self, list_id, new_name):
        self.cursor.execute("UPDATE employees SET name = ? WHERE id = ?", (new_name, list_id))
        self.connection.commit()

    def update_salary(self, list_id, new_salary):
        self.cursor.execute("UPDATE employees SET salary = ? WHERE id = ?", (new_salary, list_id))
        self.connection.commit()

    def get_max_id(self):
        self.cursor.execute("SELECT MAX(id) FROM employees")
        result = self.cursor.fetchone()
        return result[0] if result[0] is not None else 0

    def delete(self, id_to_delete):
        self.cursor.execute("DELETE FROM employees WHERE id = ?", (id_to_delete,))
        self.connection.commit()

    def close_connection(self):
        self.connection.commit()
        self.connection.close()
        print("Database connection closed.")

    def __del__(self):
        try:
            self.connection.close()
        except:
            pass

# --------- MENU STRUCTURE ---------

class Menu:

    def __init__(self):
        self.db = Database()
        self.options = {
            "1": self.list_employees,
            "2": self.add,
            "3": self.update,
            "4": self.remove,
            "0": self.exit_system
        }

    def start_menu(self):
        while True:
            print("-=" * 16)
            print("[1] - List employees")
            print("[2] - Add employee")
            print("[3] - Update table")
            print("[4] - Delete employee")
            print("[0] - Exit")
            print("-=" * 16)

            while True:
                choice = input("> ").strip()

                if choice in self.options:
                    self.options[choice]()
                    break
                else:
                    print("Invalid option, try again!")

    def list_employees(self):
        maximum = self.db.get_max_id()
        if maximum == 0:
            print("Empty list")
        else:
            records = self.db.read()
            for record in records:
                print(f"ID: {record[0]} | Name: {record[1]} | Salary: {record[2]}")

    def add(self):
        print("What name do you want to save?")
        name = input("> ")
        print("What is the salary?")
        while True:
            try:
                salary = float(input("> "))
                break
            except ValueError:
                print("Invalid value")
        self.db.save(name, salary)
        print(f"Employee {name} saved successfully!")

    def update(self):
        max_id = self.db.get_max_id()
        if max_id == 0:
            print("Empty list!")
        else:
            while True:
                print("Which employee do you want to update? (ID)")
                while True:
                    try:
                        fid = int(input("> "))
                        if fid > max_id or fid <= 0:
                            print("Invalid ID")
                        else:
                            break
                    except ValueError:
                        print("Invalid ID")
                employee = self.db.find_by_id(fid)
                if not employee:
                    print("Employee not found!")
                else:
                    print(f"ID: {employee[0]} | Name: {employee[1]} | Salary: $ {employee[2]}\n")
                    print("What do you want to update?")
                    print("[1] - Name")
                    print("[2] - Salary")
                    print("[3] - Another person")
                    print("[0] - Exit")
                    choice = input("> ")

                    if choice == "1":
                        print("What is the new name?")
                        name = input("> ")
                        self.db.update_name(fid, name)
                        return
                    elif choice == "2":
                        print("What is the new salary?")
                        while True:
                            try:
                                salary = float(input("> "))
                            except ValueError:
                                print("Invalid value.")
                            else:
                                self.db.update_salary(fid, salary)
                                return
                    elif choice == "3":
                        continue
                    elif choice == "0":
                        print("Action cancelled.")
                        return

    def remove(self):
        max_id = self.db.get_max_id()
        if max_id == 0:
            print("Empty list")
        else:
            while True:
                print("Which employee do you want to delete? (ID)")
                try:
                    eid = int(input("> "))
                    break
                except ValueError:
                    print("Invalid value")
            if eid > max_id or eid <= 0:
                print("Invalid value")
            else:
                employee = self.db.find_by_id(eid)
                if not employee:
                    print("Employee not found!")
                else:
                    print(f"ID: {employee[0]} | Name: {employee[1]} | Salary: $ {employee[2]}\n")
                    print("Are you sure you want to delete? (Y/N)")
                    while True:
                        choice = input("> ").title().strip()
                        if choice == "Y":
                            print("Employee deleted!")
                            self.db.delete(eid)
                            return
                        elif choice == "N":
                            print("Action cancelled.")
                            return
                        else:
                            print("Invalid value")

    def exit_system(self):
        print("Exiting and closing database...")
        self.db.close_connection()
        exit()

if __name__ == "__main__":
    app = Menu()
    app.start_menu()
