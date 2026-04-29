contacts = []

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter name: ")
        contacts.append(name)
        print("Contact added")

    elif choice == '2':
        print("Contacts:", contacts)

    elif choice == '3':
        search = input("Enter name to search: ")
        if search in contacts:
            print("Contact found")
        else:
            print("Not found")

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice")