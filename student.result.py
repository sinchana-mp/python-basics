m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

total = m1 + m2 + m3
avg = total / 3

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")

print("Total:", total)
print("Average:", avg)