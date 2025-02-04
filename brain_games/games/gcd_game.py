from math import gcd
from random import randint
from brain_games.games.brain_welcome import welcome_user

from brain_games.games.logic_gcd import game


def gcd_game():
	
	def rule():
		print('Find the greatest common divisor of given numbers.')

	def query():
		n1 = randint(1, 100)
		n2 = randint(1, 100)
		correct_answer = gcd(n1, n2)
		question1 = n1 + ' ' + n2
		return correct_answer, question1
		
	game(rule, query, welcome_user)