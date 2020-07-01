#!/usr/bin/env python3
import pprint

import requests


def main():
    question_request = requests.get("http://jservice.io/api/random?count=10")

    questions = question_request.json()
    pprint.pprint(questions)
    number_of_questions = len(questions)

    user_score = 0

    while number_of_questions > 0:
        current_question = questions[number_of_questions - 1]["question"]
        current_answer = questions[number_of_questions - 1]["answer"].lower().strip()

        print(current_question)
        user_answer = input("What is your answer?").lower().strip()

        if user_answer == current_answer:
            print("Congratulations! Your answer is correct!")
            number_of_questions = number_of_questions - 1
            user_score = user_score + 1

            print(f"Your current score is {user_score}.\n")
        else:
            print(
                f"Your answer is incorrect! The correct answer is {current_answer}.\nMoving on...\n"
            )

            number_of_questions = number_of_questions - 1

    print(f"Oh my you are smart!")
    print(f"Your final score is {user_score}.")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()