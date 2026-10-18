
def display_question(question_data, question_number, total_questions):
    print("\nQuestion", question_number, "of", total_questions)
    print(question_data["question"])

    for option, text in question_data["options"].items():
        print(option + ".", text)


def validate_answer(answer, options):
    answer = answer.strip().upper()
    return answer in options


def check_answer(answer, correct_answer):
    return answer == correct_answer


def update_score(score, is_correct):
    if is_correct:
        score["correct"] += 1
    else:
        score["incorrect"] += 1


def get_result_category(percentage):
    if percentage >= 80:
        return "Excellent!"
    elif percentage >= 60:
        return "Good!"
    elif percentage >= 40:
        return "Fair!"
    else:
        return "Needs Improvement."


def display_final_results(score, total_questions):
    percentage = (score["correct"] / total_questions) * 100

    print("\n========== FINAL RESULTS ==========")
    print("Total Questions:", total_questions)
    print("Correct Answers:", score["correct"])
    print("Incorrect Answers:", score["incorrect"])
    print("Final Score:", str(score["correct"]) + "/" + str(total_questions))
    print("Percentage:", round(percentage, 2), "%")
    print("Result Category:", get_result_category(percentage))
    print("===================================")


def play_quiz():
    questions = [
        {
            "question": "Which language is used to write Python programs?",
            "options": {
                "A": "HTML",
                "B": "Python",
                "C": "CSS",
                "D": "SQL"
            },
            "correct_answer": "B"
        },
        {
            "question": "Which data type stores True or False?",
            "options": {
                "A": "String",
                "B": "Integer",
                "C": "Boolean",
                "D": "List"
            },
            "correct_answer": "C"
        },
        {
            "question": "Which keyword defines a function in Python?",
            "options": {
                "A": "function",
                "B": "define",
                "C": "fun",
                "D": "def"
            },
            "correct_answer": "D"
        },
        {
            "question": "Which symbol is used for comments in Python?",
            "options": {
                "A": "#",
                "B": "//",
                "C": "<!--",
                "D": "**"
            },
            "correct_answer": "A"
        },
        {
            "question": "Which method adds an item to the end of a list?",
            "options": {
                "A": "add()",
                "B": "append()",
                "C": "insert_end()",
                "D": "push()"
            },
            "correct_answer": "B"
        }
    ]

    score = {
        "correct": 0,
        "incorrect": 0
    }

    total_questions = len(questions)

    print("\n========== PYTHON QUIZ ==========")
    print("Choose A, B, C, or D.")
    print("You can enter lowercase or uppercase letters.")

    for number, question_data in enumerate(questions, start=1):
        display_question(question_data, number, total_questions)

        while True:
            answer = input("Your answer: ").strip().upper()

            if validate_answer(answer, question_data["options"]):
                break

            print("Invalid option! Please enter A, B, C, or D.")

        if check_answer(answer, question_data["correct_answer"]):
            print("Correct! Well done!")
            update_score(score, True)
        else:
            print("Incorrect!")
            print("Correct answer:", question_data["correct_answer"])
            update_score(score, False)

    display_final_results(score, total_questions)


while True:
    play_quiz()

    play_again = input("\nWould you like to play again? (yes/no): ")
    if play_again.strip().lower() not in ["yes", "y"]:
        print("Thanks for playing! Goodbye!")
        break
