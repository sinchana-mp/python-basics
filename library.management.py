class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book, "added successfully")

    def view_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print("-", book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "removed successfully")
        else:
            print("Book not found")

library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Remove Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        book = input("Enter book name to remove: ")
        library.remove_book(book)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")