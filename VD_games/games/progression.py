from random import randint

description = "What number is missing in the progression?"

def make_progression(start, step, length):
    progression = []
    for i in range(length):
        progression.append(start + i * step)
    return progression

def get_quest_and_answer():
    start  = randint(1, 20)
    step   = randint(1, 20)
    length = randint(1, 20)

    progression = make_progression(start, step, length)

    hidden_index = randint(0, length - 1)
    correct = progression[hidden_index]

    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))

    return question, correct