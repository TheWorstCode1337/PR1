from random import randint
from prompt import string

ROUND = 3

def even_game(name:str):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    for _ in range(ROUND):
        number = randint(1, 100)
        print(f"Question: {number}")
        answer = string("Your answer: ")
        correct = "yes" if number % 2 == 0 else "no"
        
        if answer != correct:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'")
            print(f"Let's try again, {name}")
            return
        print("Correct")
        
    print(f"Congratulations. {name}")