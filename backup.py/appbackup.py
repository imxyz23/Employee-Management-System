# from flask import Flask, render_template, request, redirect, session
# from database.db import (
#     create_database,
#     add_employee,
#     get_employees,
#     delete_employee,
#     get_employee,
#     update_employee,
#     get_dashboard_data
# )

# app = Flask(__name__)
# app.secret_key = "employee_management_secret"

# create_database()


# # ---------------- LOGIN ----------------
# @app.route("/")
# def login():
#     return render_template("login.html")


# # ---------------- DASHBOARD ----------------
# @app.route("/dashboard")
# def dashboard():

#     total_employees, total_departments, total_salary = get_dashboard_data()

#     return render_template(
#         "dashboard.html",
#         total_employees=total_employees,
#         total_departments=total_departments,
#         total_salary=total_salary
#     )


# # ---------------- EMPLOYEES ----------------
# @app.route("/employees")
# def employees():

#     search = request.args.get("search", "")

#     employees = get_employees(search)

#     return render_template(
#         "employees.html",
#         employees=employees,
#         search=search
#     )


# # ---------------- ADD ----------------
# @app.route("/add_employee", methods=["POST"])
# def add():

#     name = request.form["name"]
#     department = request.form["department"]
#     salary = request.form["salary"]

#     add_employee(name, department, salary)

#     return redirect("/employees")


# # ---------------- DELETE ----------------
# @app.route("/delete/<int:id>")
# def delete(id):

#     delete_employee(id)

#     return redirect("/employees")


# # ---------------- EDIT ----------------
# @app.route("/edit/<int:id>")
# def edit(id):

#     employee = get_employee(id)

#     return render_template("edit_employee.html", employee=employee)


# # ---------------- UPDATE ----------------
# @app.route("/update/<int:id>", methods=["POST"])
# def update(id):

#     name = request.form["name"]
#     department = request.form["department"]
#     salary = request.form["salary"]

#     update_employee(id, name, department, salary)

#     return redirect("/employees")


# # ---------------- ATTENDANCE ----------------
# @app.route("/attendance")
# def attendance():
#     return render_template("attendance.html")


# @app.route("/leave")
# def leave():
#     return render_template("leave.html")


# @app.route("/payroll")
# def payroll():
#     return render_template("payroll.html")



# @app.route("/performance")
# def performance():
#     return render_template("performance.html")



# # ---------------- RUN ----------------
# if __name__ == "__main__":
#     app.run(debug=True)




