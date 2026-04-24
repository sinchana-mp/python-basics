numbers = [10, 20, 30, 40, 50]

key = int(input("Enter number to search: "))
found = False

for num in numbers:
    if num == key:
        found = True
        break

if found:
    print("Number found")
else:
    print("Number not found")