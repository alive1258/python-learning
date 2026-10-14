class Bus:
    def info(self):
        return "This is a Bus."


class Truck:
    def info(self):
        return "This is a Truck."


class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "bus":
            return Bus()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError("Unknown vehicle type")


vehicle1 = VehicleFactory.create_vehicle("bus")
vehicle2 = VehicleFactory.create_vehicle("truck")

print(vehicle1.info())
print(vehicle2.info())