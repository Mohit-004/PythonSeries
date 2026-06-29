# -------------------------------
# Python Quiz Game
# -------------------------------

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Pune", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for AI?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. Excel"],
        "answer": "A"
    },
    {
        "question": "5 + 7 = ?",
        "options": ["A. 10", "B. 12", "C. 15", "D. 11"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function?",
        "options": ["A. function", "B. fun", "C. def", "D. create"],
        "answer": "C"
    },
    {
        "question": "Which data type stores unique values?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "D"
    }
]


def start_quiz():
    score = 0

    print("=" * 40)
    print("        PYTHON QUIZ GAME")
    print("=" * 40)

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}")
        print(q["question"])

        for option in q["options"]:
            print(option)

        ans = input("Enter your answer (A/B/C/D): ").upper()

        if ans == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print("\nQuiz Completed!")
    print(f"Your Score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Grade: A")
    elif percentage >= 60:
        print("Grade: B")
    elif percentage >= 40:
        print("Grade: C")
    else:
        print("Grade: Fail...!")


start_quiz()