from math import gcd
from random import randint

from brain_games.all_logic import game


def gcd_game():
	
	def rule():
		print('Find the greatest common divisor of given numbers.')

	def query():
		n1 = randint(1, 100)
		n2 = randint(1, 100)
		correct_answer = gcd(n1, n2)
		question = str(n1) + ' ' + str(n2)
		return question, correct_answer
		
	game(rule, query)