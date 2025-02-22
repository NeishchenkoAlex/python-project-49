from random import randint

from brain_games.all_logic import game


def progression_game():
    def rule():
        print('What number is missing in the progression?')
        
    def query():
        progression = []
        current_number = randint(1, 100)
        gap = randint(1, 100)

        for _ in range(10):
            progression.append(str(current_number))
            current_number += gap

        index = randint(0, 9)
        correct_answer = str(progression.pop(index))

        progression.insert(index, '..')
        question = ' '.join(progression)

        return question, correct_answer
	
    game(rule, query)