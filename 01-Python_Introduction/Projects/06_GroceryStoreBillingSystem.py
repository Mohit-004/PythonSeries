products = {
    "Rice": 50,
    "Sugar": 45,
    "Milk": 30,
    "Bread": 25,
    "Eggs": 7
}

cart = []


def view_products():
    print("\n------ Product List ------")
    for item, price in products.items():
        print(f"{item} : ₹{price}")
    print()


def buy_product():
    product = input("Enter Product Name: ")

    if product not in products:
        print("Product Not Available.\n")
        return

    quantity = int(input("Enter Quantity: "))

    total = quantity * products[product]

    cart.append({
        "product": product,
        "quantity": quantity,
        "price": products[product],
        "total": total
    })

    print("Product Added to Cart.\n")


def view_cart():
    if not cart:
        print("Cart is Empty.\n")
        return

    print("\n------ Shopping Cart ------")

    for item in cart:
        print(f"{item['product']}  Qty:{item['quantity']}  Total: ₹{item['total']}")

    print()


def remove_product():
    product = input("Enter Product Name to Remove: ")

    for item in cart:
        if item["product"].lower() == product.lower():
            cart.remove(item)
            print("Product Removed Successfully.\n")
            return

    print("Product Not Found in Cart.\n")


def generate_bill():

    if not cart:
        print("Cart is Empty.\n")
        return

    grand_total = 0

    print("\n========== BILL ==========")

    for item in cart:
        print(f"{item['product']} x {item['quantity']} = ₹{item['total']}")
        grand_total += item["total"]

    print("---------------------------")
    print(f"Total Amount : ₹{grand_total}")
    print("===========================\n")


while True:

    print("===== GROCERY STORE =====")
    print("1. View Products")
    print("2. Buy Product")
    print("3. View Cart")
    print("4. Remove Product")
    print("5. Generate Bill")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        view_products()

    elif choice == "2":
        buy_product()

    elif choice == "3":
        view_cart()

    elif choice == "4":
        remove_product()

    elif choice == "5":
        generate_bill()

    elif choice == "6":
        print("Thank You for Shopping!")
        break

    else:
        print("Invalid Choice.\n")