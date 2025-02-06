from random import randint

from brain_games.all_logic import game


def prime_game():
	
    def rule():
        print('Answer "yes" if given number is prime. Otherwise answer "no".')

    def query():
        number = (randint(2, 100))
        
        question = str(number)
        
        correct_answer = 'yes'
        
        for i in range(2, number):
            if number % i == 0:
                correct_answer = 'no'

        return question, correct_answer

    game(rule, query)
