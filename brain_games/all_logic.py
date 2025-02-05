def game(rule, query):
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    ROUNDS = 3

    rule()

    for _ in range(ROUNDS):

        question, correct_answer = query()

        print(f'Question: {question}')
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')