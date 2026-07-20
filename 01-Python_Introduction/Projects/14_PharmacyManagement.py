# Pharmacy Management System

medicines = []


def add_medicine():

    medicine_id = input("Enter Medicine ID: ")

    for medicine in medicines:
        if medicine["id"] == medicine_id:
            print("Medicine ID already exists!")
            return

    name = input("Enter Medicine Name: ")
    price = float(input("Enter Price: "))
    stock = int(input("Enter Stock Quantity: "))

    medicines.append({
        "id": medicine_id,
        "name": name,
        "price": price,
        "stock": stock
    })

    print("Medicine Added Successfully!")


def view_medicines():

    if len(medicines) == 0:
        print("No Medicines Available.")
        return

    print("\n========== MEDICINE LIST ==========")

    for medicine in medicines:
        print(f"Medicine ID : {medicine['id']}")
        print(f"Name        : {medicine['name']}")
        print(f"Price       : ₹{medicine['price']}")
        print(f"Stock       : {medicine['stock']}")
        print("-" * 35)


def search_medicine():

    medicine_id = input("Enter Medicine ID: ")

    for medicine in medicines:
        if medicine["id"] == medicine_id:

            print("\nMedicine Found")
            print(f"Medicine ID : {medicine['id']}")
            print(f"Name        : {medicine['name']}")
            print(f"Price       : ₹{medicine['price']}")
            print(f"Stock       : {medicine['stock']}")
            return

    print("Medicine Not Found!")


def update_medicine():

    medicine_id = input("Enter Medicine ID: ")

    for medicine in medicines:
        if medicine["id"] == medicine_id:

            medicine["name"] = input("Enter New Name: ")
            medicine["price"] = float(input("Enter New Price: "))
            medicine["stock"] = int(input("Enter New Stock: "))

            print("Medicine Updated Successfully!")
            return

    print("Medicine Not Found!")


def delete_medicine():

    medicine_id = input("Enter Medicine ID: ")

    for medicine in medicines:
        if medicine["id"] == medicine_id:
            medicines.remove(medicine)
            print("Medicine Deleted Successfully!")
            return

    print("Medicine Not Found!")


def sell_medicine():

    medicine_id = input("Enter Medicine ID: ")

    for medicine in medicines:
        if medicine["id"] == medicine_id:

            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("Invalid Quantity!")
                return

            if quantity > medicine["stock"]:
                print("Insufficient Stock!")
                return

            medicine["stock"] -= quantity

            bill = quantity * medicine["price"]

            print("\nMedicine Sold Successfully!")
            print(f"Total Bill : ₹{bill}")
            print(f"Remaining Stock : {medicine['stock']}")
            return

    print("Medicine Not Found!")


def restock_medicine():

    medicine_id = input("Enter Medicine ID: ")

    for medicine in medicines:
        if medicine["id"] == medicine_id:

            quantity = int(input("Enter Quantity to Add: "))

            if quantity <= 0:
                print("Invalid Quantity!")
                return

            medicine["stock"] += quantity

            print("Stock Updated Successfully!")
            print("Current Stock:", medicine["stock"])
            return

    print("Medicine Not Found!")


def total_stock_value():

    if len(medicines) == 0:
        print("No Medicines Available.")
        return

    total = 0

    print("\n========== STOCK VALUE ==========")

    for medicine in medicines:

        value = medicine["price"] * medicine["stock"]
        total += value

        print(f"{medicine['name']} : ₹{value}")

    print("-" * 35)
    print(f"Total Stock Value : ₹{total}")


while True:

    print("\n========== PHARMACY MANAGEMENT ==========")
    print("1. Add Medicine")
    print("2. View Medicines")
    print("3. Search Medicine")
    print("4. Update Medicine")
    print("5. Delete Medicine")
    print("6. Sell Medicine")
    print("7. Restock Medicine")
    print("8. Total Stock Value")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_medicine()

    elif choice == "2":
        view_medicines()

    elif choice == "3":
        search_medicine()

    elif choice == "4":
        update_medicine()

    elif choice == "5":
        delete_medicine()

    elif choice == "6":
        sell_medicine()

    elif choice == "7":
        restock_medicine()

    elif choice == "8":
        total_stock_value()

    elif choice == "9":
        print("Thank You for Using Pharmacy Management System!")
        break

    else:
        print("Invalid Choice! Please Try Again.")