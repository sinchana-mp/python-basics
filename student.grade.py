name = input("Enter student name: ")

math = int(input("Math: "))
science = int(input("Science: "))
english = int(input("English: "))
physics = int(input("Physics: "))
chemistry = int(input("Chemistry: "))
total = math + science + english + physics + chemistry

percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "F"

print("Student:", name)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)