numbers = [10, 25, 55.5, 40, 54]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)