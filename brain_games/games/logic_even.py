from brain_games.games.brain_welcome import ROUNDS, name


def game(rule, query, welcome_user):
    welcome_user()

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