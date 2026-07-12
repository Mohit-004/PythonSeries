import random


def play_game():
    choices = ["rock", "paper", "scissors"]

    user_score = 0
    computer_score = 0

    while True:
        print("\n===== ROCK PAPER SCISSORS =====")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Show Score")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "5":
            print("\nGame Over!")
            break

        if choice == "4":
            print(f"\nYour Score     : {user_score}")
            print(f"Computer Score : {computer_score}")
            continue

        if choice not in ["1", "2", "3"]:
            print("Invalid Choice!")
            continue

        user = choices[int(choice) - 1]
        computer = random.choice(choices)

        print(f"\nYou Chose      : {user}")
        print(f"Computer Chose : {computer}")

        if user == computer:
            print("It's a Draw!")

        elif (
            (user == "rock" and computer == "scissors")
            or (user == "paper" and computer == "rock")
            or (user == "scissors" and computer == "paper")
        ):
            print("You Win!")
            user_score += 1

        else:
            print("Computer Wins!")
            computer_score += 1

    print("\n===== FINAL SCORE =====")
    print("Your Score     :", user_score)
    print("Computer Score :", computer_score)

    if user_score > computer_score:
        print("Congratulations! You Won the Game.")

    elif computer_score > user_score:
        print("Computer Won the Game.")

    else:
        print("The Game is a Draw.")


play_game()