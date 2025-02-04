import random

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ")

        if (number % 2 == 0 and answer.lower() == "yes") or (number % 2 != 0 and answer.lower() == "no"):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {'yes' if number % 2 == 0 else 'no'}.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")