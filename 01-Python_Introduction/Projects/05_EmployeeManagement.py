employees = []


def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)
    print("Employee Added Successfully.\n")


def view_employees():
    if not employees:
        print("No Employees Found.\n")
        return

    print("\n------ Employee List ------")

    for emp in employees:
        print(f"ID         : {emp['id']}")
        print(f"Name       : {emp['name']}")
        print(f"Department : {emp['department']}")
        print(f"Salary     : ₹{emp['salary']}")
        print("----------------------------")


def search_employee():
    name = input("Enter Employee Name: ").lower()

    for emp in employees:
        if emp["name"].lower() == name:
            print("\nEmployee Found")
            print(emp)
            return

    print("Employee Not Found.\n")


def update_salary():
    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:
            new_salary = float(input("Enter New Salary: "))
            emp["salary"] = new_salary
            print("Salary Updated Successfully.\n")
            return

    print("Employee Not Found.\n")


def delete_employee():
    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("Employee Deleted Successfully.\n")
            return

    print("Employee Not Found.\n")


def highest_salary():
    if not employees:
        print("No Employees Available.\n")
        return

    highest = employees[0]

    for emp in employees:
        if emp["salary"] > highest["salary"]:
            highest = emp

    print("\nHighest Paid Employee")
    print(f"Name   : {highest['name']}")
    print(f"Salary : ₹{highest['salary']}\n")


while True:

    print("========== EMPLOYEE MANAGEMENT ==========")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Highest Salary")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_salary()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        highest_salary()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.\n")