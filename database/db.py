import sqlite3


def create_database():
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        salary INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def add_employee(name, department, salary):
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO employees(name, department, salary) VALUES (?, ?, ?)",
        (name, department, salary)
    )

    conn.commit()
    conn.close()


def get_employees(search=""):
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    if search == "":
        cursor.execute("SELECT * FROM employees")
    else:
        cursor.execute("""
            SELECT * FROM employees
            WHERE name LIKE ?
            OR department LIKE ?
        """, ('%' + search + '%', '%' + search + '%'))

    employees = cursor.fetchall()

    conn.close()
    return employees


def get_employee(emp_id):
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM employees WHERE id=?",
        (emp_id,)
    )

    employee = cursor.fetchone()

    conn.close()
    return employee


def update_employee(emp_id, name, department, salary):
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE employees
        SET name=?,
            department=?,
            salary=?
        WHERE id=?
    """, (name, department, salary, emp_id))

    conn.commit()
    conn.close()


def delete_employee(emp_id):
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE id=?",
        (emp_id,)
    )

    conn.commit()
    conn.close()


def get_dashboard_data():
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM employees")
    total_employees = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT department) FROM employees")
    total_departments = cursor.fetchone()[0]

    cursor.execute("SELECT IFNULL(SUM(salary),0) FROM employees")
    total_salary = cursor.fetchone()[0]

    conn.close()

    return total_employees, total_departments, total_salary

    cursor.execute("SELECT COUNT(*) FROM employees")
    count = cursor.fetchone()[0]

    if count == 0:
        employees = [
            ("Pawan Sharma","IT",80000),
            ("Rohit Kumar","IT",75000),
            ("Aman Gupta","HR",45000),
            ("Rahul Singh","Finance",60000),
            ("Priya Verma","Marketing",55000),
            ("Sneha Patel","Sales",50000),
            ("Ankit Mishra","IT",70000),
            ("Neha Sharma","HR",48000),
            ("Vikas Yadav","Finance",65000),
            ("Simran Kaur","Marketing",52000),
            ("Arjun Mehta","Sales",47000),
            ("Karan Malhotra","IT",90000),
            ("Riya Sharma","HR",46000),
            ("Deepak Kumar","Finance",62000),
            ("Sakshi Gupta","Marketing",53000),
            ("Nitin Verma","Sales",49000),
            ("Aditi Singh","IT",78000),
            ("Mohit Jain","HR",51000),
            ("Harsh Agarwal","Finance",68000),
            ("Kavya Sharma","Marketing",56000)
        ]

        cursor.executemany(
            "INSERT INTO employees(name, department, salary) VALUES(?,?,?)",
            employees
        )