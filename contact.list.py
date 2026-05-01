# Contact Book with File Handling

file_name = "contacts.txt"

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter name: ")

        with open(file_name, "a") as f:
            f.write(name + "\n")

        print("Contact saved")

    elif choice == '2':
        try:
            with open(file_name, "r") as f:
                data = f.read()
                print("\nSaved Contacts:")
                print(data)
        except FileNotFoundError:
            print("No contacts found")

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice")