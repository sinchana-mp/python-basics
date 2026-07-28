class Student:
    def __init__(self, name, usn, marks):
        self.name = name
        self.usn = usn
        self.marks = marks

    def display(self):
        print("\n----- Student Details -----")
        print("Name :", self.name)
        print("USN  :", self.usn)
        print("Marks:", self.marks)

name = input("Enter Name: ")
usn = input("Enter USN: ")
marks = int(input("Enter Marks: "))

student1 = Student(name, usn, marks)
student1.display()