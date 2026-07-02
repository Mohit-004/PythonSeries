library = []


def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "Available"
    }

    library.append(book)
    print("Book Added Successfully.\n")


def view_books():
    if not library:
        print("No Books Available.\n")
        return

    print("\n----------- Library Books -----------")

    for book in library:
        print("Book ID :", book["id"])
        print("Title   :", book["title"])
        print("Author  :", book["author"])
        print("Status  :", book["status"])
        print("----------------------------------")


def search_book():
    name = input("Enter Book Title: ").lower()

    found = False

    for book in library:
        if book["title"].lower() == name:
            print("\nBook Found")
            print("Book ID :", book["id"])
            print("Author  :", book["author"])
            print("Status  :", book["status"])
            found = True

    if not found:
        print("Book Not Found.")

    print()


def issue_book():
    name = input("Enter Book Title: ").lower()

    for book in library:
        if book["title"].lower() == name:

            if book["status"] == "Available":
                book["status"] = "Issued"
                print("Book Issued Successfully.")
            else:
                print("Book Already Issued.")

            return

    print("Book Not Found.\n")


def return_book():
    name = input("Enter Book Title: ").lower()

    for book in library:
        if book["title"].lower() == name:

            if book["status"] == "Issued":
                book["status"] = "Available"
                print("Book Returned Successfully.")
            else:
                print("Book is Already Available.")

            return

    print("Book Not Found.\n")


def delete_book():
    name = input("Enter Book Title: ").lower()

    for book in library:
        if book["title"].lower() == name:
            library.remove(book)
            print("Book Deleted Successfully.\n")
            return

    print("Book Not Found.\n")


def available_books():

    books = [book for book in library if book["status"] == "Available"]

    if not books:
        print("No Available Books.\n")
        return

    print("\nAvailable Books")

    for book in books:
        print(book["title"])

    print()


while True:

    print("\n========== LIBRARY MANAGEMENT ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Available Books")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        delete_book()

    elif choice == "7":
        available_books()

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")