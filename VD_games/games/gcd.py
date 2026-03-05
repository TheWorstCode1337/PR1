from random import randint
from math import gcd

description = "Find the greatest common divisor of given numbers."

def get_quest_and_answer():
    a = randint(1, 100)
    b = randint(1, 100)
    question = f"{a} {b}"
    correct = gcd(a,b)
    return question, correct