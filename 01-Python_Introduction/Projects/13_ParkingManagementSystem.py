# Parking Management System

TOTAL_SLOTS = 20

parking = []


def calculate_fee(vehicle_type, hours):
    rates = {
        "bike": 20,
        "car": 50,
        "bus": 100
    }

    return rates[vehicle_type.lower()] * hours


def park_vehicle():

    if len(parking) >= TOTAL_SLOTS:
        print("Parking Full!")
        return

    vehicle_no = input("Enter Vehicle Number: ")

    for vehicle in parking:
        if vehicle["vehicle_no"] == vehicle_no:
            print("Vehicle Already Parked!")
            return

    owner = input("Enter Owner Name: ")
    vehicle_type = input("Enter Vehicle Type (Bike/Car/Bus): ").lower()

    if vehicle_type not in ["bike", "car", "bus"]:
        print("Invalid Vehicle Type!")
        return

    hours = int(input("Enter Parking Hours: "))

    fee = calculate_fee(vehicle_type, hours)

    parking.append({
        "vehicle_no": vehicle_no,
        "owner": owner,
        "vehicle_type": vehicle_type,
        "hours": hours,
        "fee": fee
    })

    print("\nVehicle Parked Successfully!")
    print("Parking Fee : ₹", fee)


def remove_vehicle():

    vehicle_no = input("Enter Vehicle Number: ")

    for vehicle in parking:
        if vehicle["vehicle_no"] == vehicle_no:
            parking.remove(vehicle)
            print("Vehicle Removed Successfully!")
            return

    print("Vehicle Not Found!")


def search_vehicle():

    vehicle_no = input("Enter Vehicle Number: ")

    for vehicle in parking:

        if vehicle["vehicle_no"] == vehicle_no:

            print("\nVehicle Found")
            print("Vehicle Number :", vehicle["vehicle_no"])
            print("Owner          :", vehicle["owner"])
            print("Vehicle Type   :", vehicle["vehicle_type"].title())
            print("Hours          :", vehicle["hours"])
            print("Parking Fee    : ₹", vehicle["fee"])
            return

    print("Vehicle Not Found!")


def view_vehicles():

    if len(parking) == 0:
        print("No Vehicles Parked!")
        return

    print("\n========== PARKED VEHICLES ==========")

    for vehicle in parking:

        print("Vehicle Number :", vehicle["vehicle_no"])
        print("Owner          :", vehicle["owner"])
        print("Vehicle Type   :", vehicle["vehicle_type"].title())
        print("Hours          :", vehicle["hours"])
        print("Fee            : ₹", vehicle["fee"])
        print("-" * 35)


def parking_status():

    occupied = len(parking)
    available = TOTAL_SLOTS - occupied

    print("\n========== PARKING STATUS ==========")
    print("Total Slots     :", TOTAL_SLOTS)
    print("Occupied Slots  :", occupied)
    print("Available Slots :", available)


def calculate_revenue():

    if len(parking) == 0:
        print("No Revenue Yet!")
        return

    total = 0

    print("\n========== REVENUE REPORT ==========")

    for vehicle in parking:

        print(vehicle["vehicle_no"], "-> ₹", vehicle["fee"])
        total += vehicle["fee"]

    print("-" * 35)
    print("Total Revenue : ₹", total)


while True:

    print("\n========== PARKING MANAGEMENT ==========")
    print("1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Search Vehicle")
    print("4. View All Vehicles")
    print("5. Parking Status")
    print("6. Calculate Total Revenue")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        park_vehicle()

    elif choice == "2":
        remove_vehicle()

    elif choice == "3":
        search_vehicle()

    elif choice == "4":
        view_vehicles()

    elif choice == "5":
        parking_status()

    elif choice == "6":
        calculate_revenue()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")