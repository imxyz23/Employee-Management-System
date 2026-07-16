from flask import Flask, render_template, request, redirect, session

from database.db import (
    create_database,
    insert_sample_data,
    add_employee,
    get_employees,
    delete_employee,
    get_employee,
    update_employee,
    get_dashboard_data
)

app = Flask(__name__)
app.secret_key = "employee_management_secret"

create_database()
insert_sample_data()

# ---------------- LOGIN ----------------
@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "admin123":
        session["user"] = username
        return redirect("/dashboard")

    return render_template(
        "login.html",
        error="Invalid Username or Password"
    )


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    total_employees, total_departments, total_salary = get_dashboard_data()

    return render_template(
        "dashboard.html",
        total_employees=total_employees,
        total_departments=total_departments,
        total_salary=total_salary
    )


# ---------------- EMPLOYEES ----------------
@app.route("/employees")
def employees():

    if "user" not in session:
        return redirect("/")

    search = request.args.get("search", "")

    employees = get_employees(search)

    return render_template(
        "employees.html",
        employees=employees,
        search=search
    )


# ---------------- ADD EMPLOYEE ----------------
@app.route("/add_employee", methods=["POST"])
def add():

    if "user" not in session:
        return redirect("/")

    name = request.form["name"]
    department = request.form["department"]
    salary = request.form["salary"]

    add_employee(name, department, salary)

    return redirect("/employees")


# ---------------- DELETE ----------------
@app.route("/delete/<int:id>")
def delete(id):

    if "user" not in session:
        return redirect("/")

    delete_employee(id)

    return redirect("/employees")


# ---------------- EDIT ----------------
@app.route("/edit/<int:id>")
def edit(id):

    if "user" not in session:
        return redirect("/")

    employee = get_employee(id)

    return render_template("edit_employee.html", employee=employee)


# ---------------- UPDATE ----------------
@app.route("/update/<int:id>", methods=["POST"])
def update(id):

    if "user" not in session:
        return redirect("/")

    name = request.form["name"]
    department = request.form["department"]
    salary = request.form["salary"]

    update_employee(id, name, department, salary)

    return redirect("/employees")


# ---------------- ATTENDANCE ----------------
@app.route("/attendance")
def attendance():

    if "user" not in session:
        return redirect("/")

    employees = get_employees()

    return render_template(
        "attendance.html",
        employees=employees
    )


# ---------------- LEAVE ----------------
@app.route("/leave")
def leave():

    if "user" not in session:
        return redirect("/")

    employees = get_employees()

    return render_template(
        "leave.html",
        employees=employees
    )


# ---------------- PAYROLL ----------------
@app.route("/payroll")
def payroll():

    if "user" not in session:
        return redirect("/")

    employees = get_employees()

    return render_template(
        "payroll.html",
        employees=employees
    )


# ---------------- PERFORMANCE ----------------
@app.route("/performance")
def performance():

    if "user" not in session:
        return redirect("/")

    employees = get_employees()

    return render_template(
        "performance.html",
        employees=employees
    )


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)