text = input("Enter a string: ")

rev = text[::-1]

if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")