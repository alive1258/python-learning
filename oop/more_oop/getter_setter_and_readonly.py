
class User:
    def __init__(self, name, age, money) -> None:
        self.name = name
        self._age = age
        self.__money = money

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age
    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            raise ValueError("Age must be positive")

    # Getter for salary
    @property
    def salary(self):
        return self.__money

    # Setter for salary: add money to the current balance
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__money += value


samsu = User("kopa", 21, 12000)

# Getter
print("Name:", samsu.name)
print("Age:", samsu.age)
print("Current salary:", samsu.salary)

# Setter for age
samsu.age = 22
print("Updated age:", samsu.age)

# Setter for salary
samsu.salary = 3000
print("Updated salary:", samsu.salary)

# Private attribute access
# print(samsu.__money)  # AttributeError
