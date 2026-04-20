numbers = [10, 5.5, 5, 0, 1, 8]

largest = second = numbers[0]

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest number:", second)