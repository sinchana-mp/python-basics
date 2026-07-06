accounts = {}

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Account Holder Name: ")
        accounts[name] = 0
        print("Account created successfully!")

    elif choice == "2":
        name = input("Enter Account Holder Name: ")

        if name in accounts:
            amount = float(input("Enter Deposit Amount: "))
            accounts[name] += amount
            print("Money deposited successfully!")
        else:
            print("Account not found!")

    elif choice == "3":
        name = input("Enter Account Holder Name: ")

        if name in accounts:
            amount = float(input("Enter Withdrawal Amount: "))

            if amount <= accounts[name]:
                accounts[name] -= amount
                print("Withdrawal successful!")
            else:
                print("Insufficient Balance!")
        else:
            print("Account not found!")

    elif choice == "4":
        name = input("Enter Account Holder Name: ")

        if name in accounts:
            print("Current Balance: ₹", accounts[name])
        else:
            print("Account not found!")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")