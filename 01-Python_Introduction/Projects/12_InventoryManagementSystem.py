products = []


def add_product():
    product_id = input("Enter Product ID: ")

    for product in products:
        if product["id"] == product_id:
            print("Product ID already exists!")
            return

    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    stock = int(input("Enter Product Stock: "))

    products.append({
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    })

    print("Product Added Successfully!")


def view_products():
    if len(products) == 0:
        print("No Products Available.")
        return

    print("\n========== PRODUCT LIST ==========")

    for product in products:
        print(f"Product ID   : {product['id']}")
        print(f"Name         : {product['name']}")
        print(f"Price        : ₹{product['price']}")
        print(f"Stock        : {product['stock']}")
        print("-" * 35)


def search_product():
    product_id = input("Enter Product ID: ")

    for product in products:
        if product["id"] == product_id:
            print("\nProduct Found")
            print(f"Product ID : {product['id']}")
            print(f"Name       : {product['name']}")
            print(f"Price      : ₹{product['price']}")
            print(f"Stock      : {product['stock']}")
            return

    print("Product Not Found.")


def update_product():
    product_id = input("Enter Product ID: ")

    for product in products:
        if product["id"] == product_id:

            product["name"] = input("Enter New Product Name: ")
            product["price"] = float(input("Enter New Price: "))
            product["stock"] = int(input("Enter New Stock: "))

            print("Product Updated Successfully!")
            return

    print("Product Not Found.")


def delete_product():
    product_id = input("Enter Product ID: ")

    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            print("Product Deleted Successfully!")
            return

    print("Product Not Found.")


def buy_product():
    product_id = input("Enter Product ID: ")

    for product in products:
        if product["id"] == product_id:

            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("Invalid Quantity.")
                return

            if quantity > product["stock"]:
                print("Insufficient Stock.")
                return

            product["stock"] -= quantity

            total = quantity * product["price"]

            print("Purchase Successful!")
            print(f"Total Amount : ₹{total}")
            print(f"Remaining Stock : {product['stock']}")
            return

    print("Product Not Found.")


def restock_product():
    product_id = input("Enter Product ID: ")

    for product in products:
        if product["id"] == product_id:

            quantity = int(input("Enter Quantity to Add: "))

            if quantity <= 0:
                print("Invalid Quantity.")
                return

            product["stock"] += quantity

            print("Stock Updated Successfully!")
            print("Current Stock:", product["stock"])
            return

    print("Product Not Found.")


def total_inventory_value():
    if len(products) == 0:
        print("No Products Available.")
        return

    total = 0

    print("\n====== INVENTORY VALUE ======")

    for product in products:
        value = product["price"] * product["stock"]
        total += value

        print(f"{product['name']} : ₹{value}")

    print("-" * 35)
    print(f"Total Inventory Value : ₹{total}")


while True:

    print("\n========== INVENTORY MANAGEMENT ==========")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Buy Product")
    print("7. Restock Product")
    print("8. Total Inventory Value")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_product()

    elif choice == "5":
        delete_product()

    elif choice == "6":
        buy_product()

    elif choice == "7":
        restock_product()

    elif choice == "8":
        total_inventory_value()

    elif choice == "9":
        print("Thank You for Using Inventory Management System!")
        break

    else:
        print("Invalid Choice! Please try again.")