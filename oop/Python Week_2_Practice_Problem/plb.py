# Problem 1: Create a Product class and a Shop class.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


product1 = Product("Laptop", 50000, 5)

print(product1.name)
print(product1.price)
print(product1.quantity)

# Inside the Shop class, create a method name add_product which adds products using the Product class to the Shop class.



class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added successfully!")


shop = Shop()

product1 = Product("Laptop", 50000, 5)
product2 = Product("Mouse", 500, 10)

shop.add_product(product1)
shop.add_product(product2)


# Inside the Shop class, create a method name buy_product which is used to buy a product and check whether this product is available or not. If you successfully buy a product, then throw a Congress message.


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def buy_product(self, product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                if product.quantity > 0:
                    product.quantity -= 1
                    print(
                        f"Congratulations! You bought "
                        f"{product.name}."
                    )
                    return

                print("Sorry, product is out of stock!")
                return

        print("Sorry, product is not available!")


shop = Shop()

laptop = Product("Laptop", 50000, 2)
shop.add_product(laptop)

shop.buy_product("Laptop")
shop.buy_product("Mobile")


# What is Inheritance? Explain with examples


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")


dog = Dog("Tommy")

dog.eat()
dog.bark()


# What are Encapsulation and Access Modifiers? Explain with examples


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)
print(account.get_balance())
