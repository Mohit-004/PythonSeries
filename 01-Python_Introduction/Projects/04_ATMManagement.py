balance = 10000
pin = "1234"
transactions = []


def check_balance():
    print(f"\nCurrent Balance : ₹{balance}\n")


def deposit():
    global balance

    amount = float(input("Enter Amount to Deposit: "))

    if amount > 0:
        balance += amount
        transactions.append(f"Deposited ₹{amount}")
        print("Amount Deposited Successfully.\n")
    else:
        print("Invalid Amount.\n")


def withdraw():
    global balance

    amount = float(input("Enter Amount to Withdraw: "))

    if amount <= 0:
        print("Invalid Amount.\n")

    elif amount > balance:
        print("Insufficient Balance.\n")

    else:
        balance -= amount
        transactions.append(f"Withdrawn ₹{amount}")
        print("Please Collect Your Cash.\n")


def transaction_history():

    if len(transactions) == 0:
        print("\nNo Transactions Yet.\n")
        return

    print("\n------ Transaction History ------")

    for t in transactions:
        print(t)

    print()


def change_pin():
    global pin

    old = input("Enter Current PIN: ")

    if old == pin:
        new = input("Enter New PIN: ")
        pin = new
        print("PIN Changed Successfully.\n")
    else:
        print("Incorrect PIN.\n")


while True:

    entered_pin = input("Enter ATM PIN: ")

    if entered_pin == pin:
        break
    else:
        print("Incorrect PIN\n")


while True:

    print("========== ATM MANAGEMENT ==========")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        transaction_history()

    elif choice == "5":
        change_pin()

    elif choice == "6":
        print("Thank You for Using Our ATM.")
        break

    else:
        print("Invalid Choice.\n")