from random import choice, randint


def game(rule):
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    ROUNDS = 3
    rule()
    
    for _ in range(ROUNDS):
        random_choice = (choice([' + ', ' * ', ' - ']))
        n1 = randint(1, 100)
        n2 = randint(1, 100)
        question1 = str(n1) + random_choice + str(n2)
        if random_choice == ' + ':
            correct_answer = n1 + n2
        if random_choice == ' - ':
            correct_answer = n1 - n2
        if random_choice == ' * ':
            correct_answer = n1 * n2
        
        question = question1

        print(f'Question: {question}')
        answer = input('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"Question: {question}\n"
                  f"Your answer: {answer}.\n"
                  f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
        