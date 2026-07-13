correct_pin = 0127
balance = 10000

attempts = 3

while attempts > 0:
    pin = int(input("Enter your ATM PIN: "))

    if pin == correct_pin:
        print("PIN Verified Successfully!")

        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Available Balance: ₹", balance)

            elif choice == 2:
                amount = int(input("Enter withdrawal amount: "))

                if amount <= balance:
                    balance -= amount
                    print("Please collect your cash")
                    print("Remaining Balance: ₹", balance)
                else:
                    print("Insufficient balance")

            elif choice == 3:
                amount = int(input("Enter deposit amount: "))

                balance += amount
                print("Money deposited successfully")
                print("Updated Balance: ₹", balance)

            elif choice == 4:
                print("Thank you for using ATM")
                break

            else:
                print("Invalid choice")

        break

    else:
        attempts -= 1
        print("Wrong PIN")
        print("Attempts remaining:", attempts)

if attempts == 0:
    print("Your card is blocked")