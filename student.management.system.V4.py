class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


students = []

# Load existing students from file
try:
    with open("students.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")

            if len(data) == 2:
                name, marks = data
                students.append(Student(name, int(marks)))

except FileNotFoundError:
    pass


while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))

        student = Student(name, marks)
        students.append(student)

        with open("students.txt", "a") as f:
            f.write(f"{name},{marks}\n")

        print("Student added!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found")
        else:
            for student in students:
                student.display()
                print()

    elif choice == "3":
        search_name = input("Enter student name: ")

        found = False

        for student in students:
            if student.name.lower() == search_name.lower():
                student.display()
                found = True
                break

        if not found:
            print("Student not found")

    elif choice == "4":
        delete_name = input("Enter student name to delete: ")

        found = False

        for student in students:
            if student.name.lower() == delete_name.lower():
                students.remove(student)

                with open("students.txt", "w") as f:
                    for s in students:
                        f.write(f"{s.name},{s.marks}\n")

                print("Student deleted!")
                found = True
                break

        if not found:
            print("Student not found")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")