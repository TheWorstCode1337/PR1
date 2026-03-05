from random import randint

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def get_quest_and_answer():
    number = randint(1, 100)
    correct = "yes" if is_prime(number) else "no"
    return number, correct