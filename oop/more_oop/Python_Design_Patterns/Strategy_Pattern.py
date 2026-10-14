class StandardFare:
    def calculate(self, distance):
        return distance * 5


class ACFare:
    def calculate(self, distance):
        return distance * 8


class Ticket:
    def __init__(self, fare_strategy):
        self.fare_strategy = fare_strategy

    def calculate_fare(self, distance):
        return self.fare_strategy.calculate(distance)


standard_ticket = Ticket(StandardFare())
ac_ticket = Ticket(ACFare())

print(standard_ticket.calculate_fare(100))  # 500
print(ac_ticket.calculate_fare(100))        # 800