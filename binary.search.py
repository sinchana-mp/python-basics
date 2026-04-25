numbers = [10, 20, 30, 40, 50]

key = int(input("Enter number to search: "))

low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == key:
        found = True
        break
    elif numbers[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Number found")
else:
    print("Number not found")