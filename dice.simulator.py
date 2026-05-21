import random

while True:
    dice = random.randint(1, 6)

    print("You rolled:", dice)

    choice = input("Roll again? (yes/no): ").lower()

    if choice != "yes":
        break