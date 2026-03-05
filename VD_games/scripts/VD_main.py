from VD_games.engine import run_game
from VD_games.games.even import description as even_desc, get_quest_and_answer as even_game
from VD_games.games.calc import description as calc_desc, get_quest_and_answer as calc_game
from VD_games.games.gcd import description as gcd_desc, get_quest_and_answer as gcd_game
from VD_games.games.progression import description as progress_desc, get_quest_and_answer as progress_game
from VD_games.games.prime_number import description as prime_desc, get_quest_and_answer as prime_game

def main():
    print("Choose game:")
    print("1 - Even")
    print("2 - Calc")
    print("3 - GCD")
    print("4 - Progression")
    print("5 - Prime number")

    choice = input("Enter number: ")

    match choice:
        case "1":
            run_game(even_desc, even_game)
        case "2":
            run_game(calc_desc, calc_game)
        case "3":
            run_game(gcd_desc, gcd_game)
        case "4":
            run_game(progress_desc, progress_game)
        case "5":
            run_game(prime_desc, prime_game)
        case _:
            print("Unknown game")