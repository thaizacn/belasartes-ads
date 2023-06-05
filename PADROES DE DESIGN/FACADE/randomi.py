import random
from interfaces import Strategy

class Random(Strategy):
    def selection(self) -> str:
        options = ["Pedra", "Papel", "Tesoura"]
        return random.choice(options)