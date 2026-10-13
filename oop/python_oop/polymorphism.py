
class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print("Animal makes some sound")


class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("Meow")


class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("Woof")


class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print("Baa")


# Create objects
don = Cat("Real Don")
dog = Dog("Tommy")
goat = Goat("Billy")

# Store objects in a list
animals = [don, dog, goat]

# Use for loop
for animal in animals:
    print(animal.name)
    animal.make_sound()
