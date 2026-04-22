numbers = [1, 2, 2, 3, 4, 4, 4, 5]

freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency:", freq)