students = []


def calculate_percentage(student):
    total = student["math"] + student["science"] + student["english"]
    return total / 3


def add_student():
    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            print("Roll Number already exists!")
            return

    name = input("Enter Name: ")
    math = int(input("Math Marks: "))
    science = int(input("Science Marks: "))
    english = int(input("English Marks: "))

    students.append({
        "roll": roll,
        "name": name,
        "math": math,
        "science": science,
        "english": english
    })

    print("Student Added Successfully!")


def view_students():
    if not students:
        print("No Student Records Found.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for student in students:
        percentage = calculate_percentage(student)

        print(f"Roll No    : {student['roll']}")
        print(f"Name       : {student['name']}")
        print(f"Math       : {student['math']}")
        print(f"Science    : {student['science']}")
        print(f"English    : {student['english']}")
        print(f"Percentage : {percentage:.2f}%")
        print("-" * 30)


def search_student():
    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            print(student)
            return

    print("Student Not Found.")


def update_marks():
    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            student["math"] = int(input("New Math Marks: "))
            student["science"] = int(input("New Science Marks: "))
            student["english"] = int(input("New English Marks: "))
            print("Marks Updated Successfully!")
            return

    print("Student Not Found.")


def delete_student():
    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found.")


def show_topper():
    if not students:
        print("No Student Records.")
        return

    topper = max(students, key=calculate_percentage)

    print("\n===== TOPPER =====")
    print("Name :", topper["name"])
    print("Roll :", topper["roll"])
    print(f"Percentage : {calculate_percentage(topper):.2f}%")


def show_result():
    if not students:
        print("No Student Records.")
        return

    print("\n========== RESULTS ==========")

    for student in students:
        percentage = calculate_percentage(student)

        status = "PASS" if percentage >= 40 else "FAIL"

        print(f"{student['name']} --> {percentage:.2f}% ({status})")


while True:

    print("\n========== STUDENT RESULT MANAGEMENT ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Show Result")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        show_topper()

    elif choice == "7":
        show_result()

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")