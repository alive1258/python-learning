
class Shopping:
    # Static/Class Attributes
    cart = []
    origin = "China"

    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location

    # Instance Method
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(
            f"Buying: {item}, price: {price}, "
            f"remaining: {remaining}"
        )

    # Static Method: Does not need self or cls
    @staticmethod
    def multiply(a, b):
        result = a * b
        print(result)

    # Class Method: Receives the class as cls
    @classmethod
    def hudai_deki(cls, item):
        print(
            "Hudai deki, kintu kinmu na. "
            "AC er hawa khete asci:", item
        )
        print("Origin:", cls.origin)


basundara = Shopping("Bashundhara City", "Dhaka")

# Instance method
basundara.purchase("lungi", 777, 999)

# Class method: Calling through an object
basundara.hudai_deki("lungi")

# Class method: Calling through the class
Shopping.hudai_deki("lungi")

# Static method: Calling through the class
Shopping.multiply(4, 5)

# Static method: Calling through an object
basundara.multiply(4, 5)

# Accessing class attributes
print(Shopping.origin)
print(basundara.origin)
