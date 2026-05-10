score = 0

print("Welcome to Quiz Game!")

answer = input("What is the capital of India? ")
if answer.lower() == "delhi":
    score += 1

answer = input("What is 5 + 5? ")
if answer == "10":
    score += 1

answer = input("Which language are we learning? ")
if answer.lower() == "python":
    score += 1

print("Your score is:", score)