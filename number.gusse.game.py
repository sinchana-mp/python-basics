import random

secret = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret:
        print("Correct! You guessed it.")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")