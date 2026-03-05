from random import randint

description = 'Answer "yes" if the number is even, otherwise answer "no".'

def get_quest_and_answer():
    number = randint(1, 100)
    correct = "yes" if number % 2 == 0 else "no"
    return number, correct