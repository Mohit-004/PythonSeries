from pathlib import Path


class Book:

    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status

    def __str__(self):
        return f"{self.book_id},{self.title},{self.author},{self.status}"


class Library:

    def __init__(self):
        self.books = []
        self.file = Path("books.txt")
        self.load_books()

    def load_books(self):

        if self.file.exists():

            with open(self.file, "r") as f:

                for line in f:

                    data = line.strip().split(",")

                    if len(data) == 4:
                        self.books.append(
                            Book(data[0], data[1], data[2], data[3])
                        )

    def save_books(self):

        with open(self.file, "w") as f:

            for book in self.books:
                f.write(str(book) + "\n")

    def add_book(self):

        try:

            book_id = input("Enter Book ID : ")

            for book in self.books:
                if book.book_id == book_id:
                    print("Book ID Already Exists!")
                    return

            title = input("Enter Book Title : ")
            author = input("Enter Author Name : ")

            self.books.append(Book(book_id, title, author))

            self.save_books()

            print("Book Added Successfully!")

        except Exception as e:
            print("Error :", e)

    def view_books(self):

        if len(self.books) == 0:
            print("No Books Available.")
            return

        print("\n========== BOOK LIST ==========")

        for book in self.books:

            print("Book ID :", book.book_id)
            print("Title   :", book.title)
            print("Author  :", book.author)
            print("Status  :", book.status)
            print("-" * 35)

    def search_book(self):

        book_id = input("Enter Book ID : ")

        for book in self.books:

            if book.book_id == book_id:

                print("\nBook Found")
                print("Book ID :", book.book_id)
                print("Title   :", book.title)
                print("Author  :", book.author)
                print("Status  :", book.status)
                return

        print("Book Not Found.")

    def issue_book(self):

        book_id = input("Enter Book ID : ")

        for book in self.books:

            if book.book_id == book_id:

                if book.status == "Issued":
                    print("Book Already Issued!")
                    return

                book.status = "Issued"

                self.save_books()

                print("Book Issued Successfully!")
                return

        print("Book Not Found.")

    def return_book(self):

        book_id = input("Enter Book ID : ")

        for book in self.books:

            if book.book_id == book_id:

                if book.status == "Available":
                    print("Book is Already Available!")
                    return

                book.status = "Available"

                self.save_books()

                print("Book Returned Successfully!")
                return

        print("Book Not Found.")

    def delete_book(self):

        book_id = input("Enter Book ID : ")

        for book in self.books:

            if book.book_id == book_id:

                self.books.remove(book)

                self.save_books()

                print("Book Deleted Successfully!")
                return

        print("Book Not Found.")


library = Library()

while True:

    print("\n========== LIBRARY MANAGEMENT ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.delete_book()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
        