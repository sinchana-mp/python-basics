# Advanced Contact Book

file_name = "contacts.txt"

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        with open(file_name, "a") as f:
            f.write(name + " - " + phone + "\n")

        print("Contact saved")

    elif choice == '2':
        try:
            with open(file_name, "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("No contacts found")

    elif choice == '3':
        search_name = input("Enter name to search: ")
        found = False

        try:
            with open(file_name, "r") as f:
                for line in f:
                    if search_name.lower() in line.lower():
                        print("Found:", line)
                        found = True

            if not found:
                print("Contact not found")

        except FileNotFoundError:
            print("No contacts found")

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice")