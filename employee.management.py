class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

employee1 = Employee("Rudra", 50000)
employee2 = Employee("Sinchana", 60000)

employee1.display()
print()

employee2.display()