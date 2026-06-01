class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))

        student = Student(name, marks)
        students.append(student)

        print("Student added!")

    elif choice == "2":
        for student in students:
            student.display()
            print()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice")