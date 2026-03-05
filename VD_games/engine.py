from prompt import string
from .cli import welcome_user

def run_game(description, game_logic):
    print("Welcome to the VD-games!")
    name = welcome_user()
    print(description)
    for _ in range(3):
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        answer = string("Your answer: ")
        if answer != str(correct_answer):
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}")
            return
        print("Correct")
        
    print(f"Congratulations, {name}")