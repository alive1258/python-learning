
# Base class / Parent class
class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def move(self):
        return f"{self.name} is moving."


# Child class
class Bus(Vehicle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat
        super().__init__(name, price)

    def show_info(self):
        return (
            f"Bus: {self.name}, Price: {self.price}, "
            f"Seats: {self.seat}"
        )


class Truck(Vehicle):
    def __init__(self, name, price, weight) -> None:
        self.weight = weight
        super().__init__(name, price)

    def show_info(self):
        return (
            f"Truck: {self.name}, Price: {self.price}, "
            f"Capacity: {self.weight} tons"
        )


# Child class of Bus
class ACBus(Bus):
    def __init__(self, name, price, seat, ac_type) -> None:
        self.ac_type = ac_type
        super().__init__(name, price, seat)

    def show_info(self):
        return (
            f"AC Bus: {self.name}, Price: {self.price}, "
            f"Seats: {self.seat}, AC Type: {self.ac_type}"
        )


# Child class of Truck
class PickUpVan(Truck):
    def __init__(self, name, price, weight, cargo_type) -> None:
        self.cargo_type = cargo_type
        super().__init__(name, price, weight)

    def show_info(self):
        return (
            f"Pickup Van: {self.name}, Price: {self.price}, "
            f"Capacity: {self.weight} tons, "
            f"Cargo: {self.cargo_type}"
        )


# Create objects
bus1 = Bus("Green Line Bus", 5000000, 40)
truck1 = Truck("Heavy Truck", 8000000, 20)
ac_bus1 = ACBus("Volvo AC Bus", 9000000, 36, "Climate Control")
pickup1 = PickUpVan("Toyota Pickup", 2500000, 2, "Goods")

# Display information
print(bus1.show_info())
print(bus1.move())

print(truck1.show_info())
print(truck1.move())

print(ac_bus1.show_info())
print(ac_bus1.move())

print(pickup1.show_info())
print(pickup1.move())
