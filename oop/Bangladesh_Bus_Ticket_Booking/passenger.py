
class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus
        self.fare = 500

    def show_ticket(self):
        print("\n========== BUS TICKET ==========")
        print(f"Passenger Name: {self.name}")
        print(f"Phone Number: {self.phone}")
        print(f"Bus Number: {self.bus.number}")
        print(f"Route: {self.bus.route}")
        print(f"Ticket Fare: TK{self.fare}")
        print("================================")
