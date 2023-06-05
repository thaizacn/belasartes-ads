from interfaces import Strategy

class Papel(Strategy):
    def selection(self) -> str:
        return "Papel"