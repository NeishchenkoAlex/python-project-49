from random import randint

from brain_games.games.logic_prime import game


def prime_game():
	
    def rule():
        print('Answer "yes" if given number is prime. Otherwise answer "no".')

    def query():
        n = (randint(2, 100))
        
        question = str(n)
        
        correct_answer = 'yes'
        
        for i in range(2, n):
            if n % i == 0:
                correct_answer = 'no'

        return question, correct_answer

    game(rule, query)
