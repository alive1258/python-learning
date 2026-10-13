from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        print("I need food")

    def move(self):
        pass


class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category = "Monkey"
        self.name = name
        super().__init__()

    def eat(self):
        print("i eat bananann ")


lakey = Monkey("luckey")
lakey.eat()
