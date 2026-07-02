while True:
    print("\n===== NOTES APP =====")
    print("1. Write Note")
    print("2. Read Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note = input("Write your note: ")

        file = open("notes.txt", "a")
        file.write(note + "\n")
        file.close()

        print("Note saved successfully!")

    elif choice == "2":
        try:
            file = open("notes.txt", "r")
            print("\nYour Notes:\n")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("No notes found!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")