from VD_games.scripts.VD_game import greeter
from .VD_even import even_game

def main():
    name = greeter()
    even_game(name)