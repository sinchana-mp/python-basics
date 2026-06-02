class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))

        student = Student(name, marks)
        students.append(student)

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
        print("Exiting...")
        break

    else:
        print("Invalid choice")