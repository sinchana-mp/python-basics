import random

secret = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1

    if guess == secret:
        print("Correct!")
        print("Attempts:", attempts)
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")