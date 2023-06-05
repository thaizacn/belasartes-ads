from interfaces import Strategy

class Pedra(Strategy):
    def selection(self) -> str:
        return "Pedra"