
class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    # Method: Common behavior inherited by child classes
    def eat(self):
        print("Eats vegetarian food")

    # Method: Can be overridden in a child class
    def exercise(self):
        print("Exercises and sweats")

    # Operator Overloading: Defines the behavior of + for Person objects
    def __add__(self, other):
        return self.age + other.age

    # Operator Overloading: Defines the behavior of * for Person objects
    def __mul__(self, other):
        return self.weight * other.weight

    # Operator Overloading: Defines the behavior of < (less than)
    def __lt__(self, other):
        return self.age < other.age

    # Operator Overloading: Defines the behavior of <= (less than or equal)
    def __le__(self, other):
        return self.age <= other.age

    # Operator Overloading: Defines the behavior of == (equal to)
    def __eq__(self, other):
        return self.age == other.age

    # Operator Overloading: Defines the behavior of != (not equal to)
    def __ne__(self, other):
        return self.age != other.age

    # Operator Overloading: Defines the behavior of > (greater than)
    def __gt__(self, other):
        return self.age > other.age

    # Operator Overloading: Defines the behavior of >= (greater than or equal)
    def __ge__(self, other):
        return self.age >= other.age


class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        # Call the parent class constructor
        super().__init__(name, age, height, weight)

    # Method Overriding: Provides a specialized implementation of exercise()
    def exercise(self):
        print("Cricketer practices batting, bowling, and fitness")


sakib = Cricketer("Sakib", 27, 78, 98, "BD")
mushi = Cricketer("Mushi", 37, 58, 68, "BD")

# Method Overriding demonstration
sakib.exercise()

# Operator Overloading demonstration
print("Combined age:", sakib + mushi)
print("Weight multiplication:", sakib * mushi)
print("Sakib younger than Mushi:", sakib < mushi)
print("Same age:", sakib == mushi)
