passwords = {}


def password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special = "@#$%^&*!?"

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special:
            has_special = True

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif len(password) >= 6:
        return "Medium"
    else:
        return "Weak"


def add_account():
    website = input("Enter Website/App Name: ")

    if website in passwords:
        print("Account already exists.\n")
        return

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    passwords[website] = {
        "username": username,
        "password": password
    }

    print("Account Saved Successfully.\n")


def view_accounts():
    if not passwords:
        print("No Accounts Found.\n")
        return

    print("\n------ Saved Accounts ------")

    for website, data in passwords.items():
        print(f"Website : {website}")
        print(f"Username: {data['username']}")
        print(f"Password: {data['password']}")
        print(f"Strength: {password_strength(data['password'])}")
        print("--------------------------")

    print()


def search_account():
    website = input("Enter Website Name: ")

    if website in passwords:
        data = passwords[website]
        print("\nUsername :", data["username"])
        print("Password :", data["password"])
        print("Strength :", password_strength(data["password"]))
    else:
        print("Account Not Found.")

    print()


def update_password():
    website = input("Enter Website Name: ")

    if website in passwords:
        new_pass = input("Enter New Password: ")
        passwords[website]["password"] = new_pass
        print("Password Updated Successfully.")
    else:
        print("Account Not Found.")

    print()


def delete_account():
    website = input("Enter Website Name: ")

    if website in passwords:
        del passwords[website]
        print("Account Deleted.")
    else:
        print("Account Not Found.")

    print()


def total_accounts():
    print("Total Saved Accounts:", len(passwords))
    print()


while True:

    print("========== PASSWORD MANAGER ==========")
    print("1. Add Account")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Update Password")
    print("5. Delete Account")
    print("6. Total Accounts")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_account()

    elif choice == "2":
        view_accounts()

    elif choice == "3":
        search_account()

    elif choice == "4":
        update_password()

    elif choice == "5":
        delete_account()

    elif choice == "6":
        total_accounts()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice\n")