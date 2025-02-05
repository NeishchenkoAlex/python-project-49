from random import choice, randint

from brain_games.all_logic import game


def calc_game():
	
    def rule():
        print('What is the result of the expression?')

    def query():
        random_choice = (choice([' + ', ' * ', ' - ']))
        n1 = randint(1, 100)
        n2 = randint(1, 100)
        
        question = str(n1) + random_choice + str(n2)
        
        if random_choice == ' + ':
            correct_answer = n1 + n2
        if random_choice == ' - ':
            correct_answer = n1 - n2
        if random_choice == ' * ':
            correct_answer = n1 * n2
        return question, str(correct_answer)

    game(rule, query)
