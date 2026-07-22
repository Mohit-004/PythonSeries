from pathlib import Path


class Student:

    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.roll},{self.name},{self.marks}"


class StudentManager:

    def __init__(self):
        self.students = []
        self.file = Path("students.txt")
        self.load_students()

    def load_students(self):

        if self.file.exists():

            with open(self.file, "r") as f:

                for line in f:

                    data = line.strip().split(",")

                    if len(data) == 3:
                        self.students.append(
                            Student(data[0], data[1], int(data[2]))
                        )

    def save_students(self):

        with open(self.file, "w") as f:

            for student in self.students:
                f.write(str(student) + "\n")

    def add_student(self):

        try:

            roll = input("Enter Roll No : ")

            for student in self.students:
                if student.roll == roll:
                    print("Roll Number Already Exists!")
                    return

            name = input("Enter Name : ")
            marks = int(input("Enter Marks : "))

            self.students.append(Student(roll, name, marks))

            self.save_students()

            print("Student Added Successfully!")

        except ValueError:
            print("Marks must be numeric!")

    def view_students(self):

        if not self.students:
            print("No Records Found.")
            return

        print("\n========== STUDENTS ==========")

        for student in self.students:

            print("Roll :", student.roll)
            print("Name :", student.name)
            print("Marks:", student.marks)
            print("-" * 30)

    def search_student(self):

        roll = input("Enter Roll Number : ")

        for student in self.students:

            if student.roll == roll:

                print("\nStudent Found")
                print("Roll :", student.roll)
                print("Name :", student.name)
                print("Marks:", student.marks)
                return

        print("Student Not Found.")

    def delete_student(self):

        roll = input("Enter Roll Number : ")

        for student in self.students:

            if student.roll == roll:

                self.students.remove(student)

                self.save_students()

                print("Student Deleted Successfully!")
                return

        print("Student Not Found.")


manager = StudentManager()

while True:

    print("\n========== STUDENT MANAGEMENT ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        manager.add_student()

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        manager.search_student()

    elif choice == "4":
        manager.delete_student()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")