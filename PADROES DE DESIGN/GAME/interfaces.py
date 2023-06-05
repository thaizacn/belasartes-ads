from abc import ABC, abstractmethod

# Interface (forma de bolo)
class Strategy (ABC):
    @abstractmethod
    def selection(self) -> None:
        pass