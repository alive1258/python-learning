
# Parent class
class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        return f"Vehicle: {self.name}, Price: {self.price} BDT"


# Inheritance: Bus is a Vehicle
class Bus(Vehicle):
    def __init__(self, name, price, seats):
        super().__init__(name, price)
        self.seats = seats

    def show_info(self):
        return (
            f"Bus: {self.name}, Price: {self.price} BDT, "
            f"Seats: {self.seats}"
        )


# Composition: Computer has an Engine
class Engine:
    def __init__(self, engine_type, horsepower):
        self.engine_type = engine_type
        self.horsepower = horsepower

    def show_info(self):
        return f"{self.engine_type}, {self.horsepower} HP"


class Car(Vehicle):
    def __init__(self, name, price, engine_type, horsepower):
        super().__init__(name, price)
        self.engine = Engine(engine_type, horsepower)

    def show_info(self):
        return (
            f"Car: {self.name}, Price: {self.price} BDT, "
            f"Engine: {self.engine.show_info()}"
        )


# Association: A Driver can be assigned to a Bus
class Driver:
    def __init__(self, name, license_number):
        self.name = name
        self.license_number = license_number

    def drive(self, bus):
        if not isinstance(bus, Bus):
            raise TypeError("Driver must be assigned to a Bus.")

        return f"{self.name} is driving {bus.name}"


# Create objects
bus1 = Bus("Green Line", 5000000, 40)
car1 = Car("Toyota Corolla", 3000000, "Petrol", 138)
driver1 = Driver("Rahim", "DL-1001")

# Display information
print(bus1.show_info())
print(car1.show_info())
print(driver1.drive(bus1))
