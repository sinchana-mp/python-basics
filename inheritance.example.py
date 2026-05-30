class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def show_details(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


student = Student("Sinchana", 95)

student.show_name()
student.show_details()