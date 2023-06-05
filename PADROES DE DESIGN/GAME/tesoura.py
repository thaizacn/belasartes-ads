from interfaces import Strategy

class Tesoura(Strategy):
    def selection(self) -> str:
        return "Tesoura"