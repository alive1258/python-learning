
class Engine:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.horsepower = horsepower

    def start(self):
        return f"{self.brand} engine started!"


class Car:
    def __init__(self, brand, model, engine_brand, horsepower):
        self.brand = brand
        self.model = model

        # Composition: Car has an Engine
        self.engine = Engine(engine_brand, horsepower)

    def start_car(self):
        result = self.engine.start()
        return f"{self.brand} {self.model}: {result}"

    def show_info(self):
        return (
            f"Car: {self.brand} {self.model}\n"
            f"Engine: {self.engine.brand}\n"
            f"Horsepower: {self.engine.horsepower} HP"
        )


# Create a Car object
my_car = Car("Toyota", "Corolla", "Toyota", 138)

# Call methods
print(my_car.show_info())
print(my_car.start_car())
