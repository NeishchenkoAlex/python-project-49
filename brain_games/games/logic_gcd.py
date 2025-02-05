def game(rule, query):
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    ROUNDS = 3
    
    rule()
    
    for _ in range(ROUNDS):
        
        question, correct_answer = query()

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
        