import string

password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char in string.punctuation for char in password):
    score += 1


if score == 5:
    print("Strong Password ")
elif score >= 3:
    print("Medium Password ")
else:
    print("Weak Password ")

print("Password Score:", score, "/ 5")