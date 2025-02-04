from brain_games.games.brain_welcome import ROUNDS, name
from brain_games.games.gcd_game import correct_answer, question1


def game(rule, query, welcome_user):
    welcome_user()
    rule()
    
    for _ in range(ROUNDS):
        
        question = question1

        print(f'Question: {question}')
        answer = input('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"Question: {question}\n"
                  f"Your answer: {answer}.\n"
                  f"""'{answer}' is wrong answer ;(. 
                  Correct answer was '{correct_answer}'.\n"""
                  f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
        