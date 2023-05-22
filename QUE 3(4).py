import random

def multiplication_game():
    print("Welcome to the Multiplication Game!")
    print("Answer the following multiplication questions:")

    correct_answers = 0
    for question_number in range(1, 11):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_result = num1 * num2

        user_answer = input(f"Question {question_number}: {num1} x {num2} = ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_answer == correct_result:
            print("Right!")
            correct_answers += 1
        else:
            print(f"Wrong. The answer is {correct_result}.")

    print(f"\nGame over! You got {correct_answers} out of 10 questions correct.")

multiplication_game()