numbers = list(map(int, input("Enter numbers: ").split()))

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even count:", even)
print("Odd count:", odd)