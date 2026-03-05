from random import randint, choice

description = "What is the result of the expression?"

def get_quest_and_answer():
    a = randint(1, 50)
    b = randint(1, 50)
    operator = choice(["+", "-", "*"])

    match operator:
        case "+":
            correct = a + b
        case "-":
            correct = a - b
        case "*":
            correct = a * b
    question = f"{a} {operator} {b}"

    return question, correct