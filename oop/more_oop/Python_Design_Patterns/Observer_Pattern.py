class Observer:
    def update(self, message):
        raise NotImplementedError


class Passenger(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received: {message}")


class BusService:
    def __init__(self):
        self.passengers = []

    def subscribe(self, passenger):
        self.passengers.append(passenger)

    def notify(self, message):
        for passenger in self.passengers:
            passenger.update(message)


service = BusService()

service.subscribe(Passenger("Rahim"))
service.subscribe(Passenger("Karim"))

service.notify("Your bus will depart in 10 minutes.")