from math import gcd
from random import randint

from brain_games.all_logic import game


def gcd_game():
	
	def rule():
		print('Find the greatest common divisor of given numbers.')

	def query():
		number_1 = randint(1, 100)
		number_2 = randint(1, 100)
		correct_answer = gcd(number_1, number_2)
		question = str(number_1) + ' ' + str(number_2)
		return question, str(correct_answer)
		
	game(rule, query)