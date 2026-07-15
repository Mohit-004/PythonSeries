candidates = {
    "1": {
        "name": "Rahul",
        "votes": 0
    },
    "2": {
        "name": "Amit",
        "votes": 0
    },
    "3": {
        "name": "Sneha",
        "votes": 0
    }
}

voted_users = set()


def show_candidates():
    print("\n===== CANDIDATES =====")

    for candidate_id, data in candidates.items():
        print(f"{candidate_id}. {data['name']}")


def vote():
    voter_id = input("Enter Voter ID: ")

    if voter_id in voted_users:
        print("You have already voted!")
        return

    show_candidates()

    choice = input("Enter Candidate Number: ")

    if choice not in candidates:
        print("Invalid Candidate!")
        return

    candidates[choice]["votes"] += 1
    voted_users.add(voter_id)

    print("Vote Submitted Successfully!")


def show_results():
    print("\n===== VOTING RESULTS =====")

    for data in candidates.values():
        print(f"{data['name']} : {data['votes']} Votes")


def show_winner():
    if len(voted_users) == 0:
        print("No Votes Available!")
        return

    highest_votes = max(
        data["votes"]
        for data in candidates.values()
    )

    winners = [
        data["name"]
        for data in candidates.values()
        if data["votes"] == highest_votes
    ]

    print("\n===== ELECTION RESULT =====")

    if len(winners) == 1:
        print("Winner:", winners[0])
        print("Total Votes:", highest_votes)

    else:
        print("Election is Tied!")
        print("Candidates:", ", ".join(winners))
        print("Votes:", highest_votes)


def total_votes():
    print("Total Votes:", len(voted_users))


while True:

    print("\n========== VOTING SYSTEM ==========")
    print("1. Show Candidates")
    print("2. Vote")
    print("3. Show Results")
    print("4. Show Winner")
    print("5. Total Votes")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        show_candidates()

    elif choice == "2":
        vote()

    elif choice == "3":
        show_results()

    elif choice == "4":
        show_winner()

    elif choice == "5":
        total_votes()

    elif choice == "6":
        print("Voting System Closed.")
        break

    else:
        print("Invalid Choice!")