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

total = math + science + english + physics + chemistry
percentage = total / 5

print("\n----- Result -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

if percentage >= 35:
    status = "PASS"
else:
    status = "FAIL"

print("Grade:", grade)
print("Status:", status)

print("\n" + "=" * 35)
print("      STUDENT REPORT CARD")
print("=" * 35)
print("Student Name :", name)
print("Math         :", math)
print("Science      :", science)
print("English      :", english)
print("Physics      :", physics)
print("Chemistry    :", chemistry)
print("-" * 35)
print("Total Marks  :", total)
print("Percentage   :", f"{percentage:.2f}%")
print("Grade        :", grade)
print("Status       :", status)
print("=" * 35)

again = input("\nDo you want to enter another student's result? (yes/no): ")