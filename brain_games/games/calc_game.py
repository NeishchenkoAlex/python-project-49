from random import choice, randint

from brain_games.all_logic import game


def calc_game():
	
    def rule():
        print('What is the result of the expression?')

    def query():
        arithmetic_signs = [' + ', ' * ', ' - ']
        random_signs = (choice(arithmetic_signs))
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        
        question = str(number_1) + random_signs + str(number_2)
        
        if random_signs == ' + ':
            correct_answer = number_1 + number_2
        if random_signs == ' - ':
            correct_answer = number_1 - number_2
        if random_signs == ' * ':
            correct_answer = number_1 * number_2
        return question, str(correct_answer)

    game(rule, query)
