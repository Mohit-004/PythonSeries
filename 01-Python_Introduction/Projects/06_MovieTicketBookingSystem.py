movies = {
    "Avengers": 20,
    "Leo": 15,
    "Pushpa": 25,
    "KGF": 18
}

bookings = []


def view_movies():
    print("\n------ Movies ------")
    for movie, seats in movies.items():
        print(f"{movie} - Available Seats: {seats}")
    print()


def book_ticket():
    movie = input("Enter Movie Name: ")

    if movie not in movies:
        print("Movie Not Found.\n")
        return

    if movies[movie] == 0:
        print("No Seats Available.\n")
        return

    name = input("Enter Customer Name: ")
    tickets = int(input("Enter Number of Tickets: "))

    if tickets <= movies[movie]:
        movies[movie] -= tickets

        bookings.append({
            "name": name,
            "movie": movie,
            "tickets": tickets
        })

        print("Ticket Booked Successfully.\n")
    else:
        print("Not Enough Seats Available.\n")


def cancel_ticket():
    name = input("Enter Customer Name: ")

    for booking in bookings:
        if booking["name"].lower() == name.lower():

            movies[booking["movie"]] += booking["tickets"]
            bookings.remove(booking)

            print("Booking Cancelled Successfully.\n")
            return

    print("Booking Not Found.\n")


def search_booking():
    name = input("Enter Customer Name: ")

    for booking in bookings:
        if booking["name"].lower() == name.lower():
            print("\nBooking Details")
            print(f"Name   : {booking['name']}")
            print(f"Movie  : {booking['movie']}")
            print(f"Tickets: {booking['tickets']}")
            return

    print("Booking Not Found.\n")


def available_seats():
    print("\nAvailable Seats")
    for movie, seats in movies.items():
        print(f"{movie}: {seats}")
    print()


def view_bookings():
    if not bookings:
        print("No Bookings Yet.\n")
        return

    print("\n------ All Bookings ------")

    for booking in bookings:
        print(f"Customer : {booking['name']}")
        print(f"Movie    : {booking['movie']}")
        print(f"Tickets  : {booking['tickets']}")
        print("--------------------------")


while True:

    print("========== MOVIE TICKET BOOKING ==========")
    print("1. View Movies")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. Search Booking")
    print("5. Available Seats")
    print("6. View All Bookings")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        view_movies()

    elif choice == "2":
        book_ticket()

    elif choice == "3":
        cancel_ticket()

    elif choice == "4":
        search_booking()

    elif choice == "5":
        available_seats()

    elif choice == "6":
        view_bookings()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.\n")