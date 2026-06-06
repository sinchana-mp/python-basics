website = input("Enter website: ")
password = input("Enter password: ")

with open("passwords.txt", "a") as f:
    f.write(f"{website} : {password}\n")

print("Password saved!")