from random import randint

from brain_games.scripts.logic import game


def even_game():
	
	def rule():
		print('Answer "yes" if the number is even, otherwise answer "no".')

	def query():
		question = randint(1, 100)
		correct_answer = 'yes' if question % 2 == 0 else 'no'
		return question, correct_answer
	
	game(rule, query)