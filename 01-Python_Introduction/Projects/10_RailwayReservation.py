trains = {
    "101": {
        "name": "Rajdhani Express",
        "seats": 5
    },
    "102": {
        "name": "Shatabdi Express",
        "seats": 4
    },
    "103": {
        "name": "Duronto Express",
        "seats": 6
    }
}

bookings = []


def view_trains():

    print("\n========== TRAIN LIST ==========")

    for train_id, train in trains.items():
        print(f"Train No : {train_id}")
        print(f"Train    : {train['name']}")
        print(f"Seats    : {train['seats']}")
        print("----------------------------")


def book_ticket():

    train_id = input("Enter Train Number: ")

    if train_id not in trains:
        print("Invalid Train Number.\n")
        return

    if trains[train_id]["seats"] == 0:
        print("No Seats Available.\n")
        return

    passenger = input("Enter Passenger Name: ")
    age = int(input("Enter Age: "))

    trains[train_id]["seats"] -= 1

    bookings.append({
        "name": passenger,
        "age": age,
        "train": trains[train_id]["name"],
        "train_no": train_id
    })

    print("Ticket Booked Successfully.\n")


def view_bookings():

    if len(bookings) == 0:
        print("No Bookings Found.\n")
        return

    print("\n========== BOOKINGS ==========")

    for booking in bookings:
        print(f"Passenger : {booking['name']}")
        print(f"Age       : {booking['age']}")
        print(f"Train     : {booking['train']}")
        print(f"Train No  : {booking['train_no']}")
        print("---------------------------")


def search_booking():

    name = input("Enter Passenger Name: ").lower()

    for booking in bookings:

        if booking["name"].lower() == name:

            print("\nBooking Found")
            print(f"Passenger : {booking['name']}")
            print(f"Train     : {booking['train']}")
            print(f"Train No  : {booking['train_no']}")
            return

    print("Booking Not Found.\n")


def cancel_ticket():

    name = input("Enter Passenger Name: ").lower()

    for booking in bookings:

        if booking["name"].lower() == name:

            train_no = booking["train_no"]

            trains[train_no]["seats"] += 1

            bookings.remove(booking)

            print("Ticket Cancelled Successfully.\n")
            return

    print("Booking Not Found.\n")


def available_seats():

    print("\n====== AVAILABLE SEATS ======")

    for train in trains.values():
        print(f"{train['name']} : {train['seats']} Seats")


while True:

    print("\n========== RAILWAY RESERVATION ==========")
    print("1. View Trains")
    print("2. Book Ticket")
    print("3. View Bookings")
    print("4. Search Booking")
    print("5. Cancel Ticket")
    print("6. Available Seats")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        view_trains()

    elif choice == "2":
        book_ticket()

    elif choice == "3":
        view_bookings()

    elif choice == "4":
        search_booking()

    elif choice == "5":
        cancel_ticket()

    elif choice == "6":
        available_seats()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")