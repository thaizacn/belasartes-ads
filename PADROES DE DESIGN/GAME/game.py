from interfaces import Strategy
from randomi import Random
from papel import Papel
from tesoura import Tesoura
from pedra import Pedra

#Contexto (lógica do jogo)
class Game:
    strategy: Strategy

    def __init__ (self, strategy: Strategy = None) -> None:
        if strategy is not None:
            self.strategy = strategy
        else: 
            self.strategy = Random()   

    def play(self, sec) -> None:
        s1 = self.strategy.selection()
        s2 = sec.strategy.selection()
        if s1 == s2:
            print("It's a tie")
        elif s1 == "Pedra":
            if s2 == "Tesoura":
                print("Player 1 wins!")
            else: 
                print("Player 2 wins!")
        elif s1 == "Tesoura":
            if s2 == "Papel":
                print("Player 1 wins!")
            else: 
                print("Player 2 wins!")
        elif s1 == "Papel":
            if s2 == "Pedra":
                print("Player 1 wins!")
            else: 
                print("Player 2 wins!")

player1 = Game(Tesoura())
player2 = Game(Papel())

player1.play(player2)