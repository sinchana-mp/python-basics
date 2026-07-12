balance = 0

def number_to_words(num):
    ones = [
        "", "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen",
        "Fifteen", "Sixteen", "Seventeen",
        "Eighteen", "Nineteen"
    ]

    tens = [
        "", "", "Twenty", "Thirty", "Forty",
        "Fifty", "Sixty", "Seventy",
        "Eighty", "Ninety"
    ]

    if num == 0:
        return "Zero"

    if num < 20:
        return ones[num]

    if num < 100:
        return tens[num // 10] + " " + ones[num % 10]

    if num < 1000:
        return ones[num // 100] + " Hundred " + number_to_words(num % 100)

    if num < 100000:
        return number_to_words(num // 1000) + " Thousand " + number_to_words(num % 1000)

    return "Amount too large"


while True:
    print("\n--- Bank Account System ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance: ₹", balance)
        print("In Words:", number_to_words(int(balance)), "Rupees")

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Money deposited successfully!")
        else:
            print("Invalid amount")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Money withdrawn successfully!")
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you for using Bank System")
        break

    else:
        print("Invalid choice")