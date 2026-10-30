
from bus import Bus
from passenger import Passenger


class BusSystem:
    TICKET_FARE = 500

    def __init__(self):
        self.buses = []
        self.passengers = []
        self.admin_logged_in = False

    # Add bus (admin only)
    def add_bus(self, number, route, seats):
        if not self.admin_logged_in:
            return "Access denied! Admin login required."

        if not number or not route:
            return "Bus number and route are required."

        if seats <= 0:
            return "Total seats must be greater than zero."

        for bus in self.buses:
            if bus.number == number:
                return "This bus number already exists."

        new_bus = Bus(number, route, seats)
        self.buses.append(new_bus)

        return f"Bus {number} added successfully!"

    # Book ticket
    def book_ticket(self, bus_number, name, phone):
        selected_bus = None

        for bus in self.buses:
            if bus.number == bus_number:
                selected_bus = bus
                break

        if selected_bus is None:
            return None, "Bus not found!"

        if selected_bus.available_seats() <= 0:
            return None, "Sorry! No seats available."

        if not name.strip() or not phone.strip():
            return None, "Name and phone are required."

        if not phone.isdigit() or len(phone) != 11:
            return None, "Please enter a valid 11-digit phone number."

        if selected_bus.book_seat():
            passenger = Passenger(name, phone, selected_bus)
            self.passengers.append(passenger)

            return passenger, "Ticket booked successfully!"

        return None, "Booking failed!"

    # View all buses
    def show_buses(self):
        print("\n========== AVAILABLE BUSES ==========")

        if not self.buses:
            print("No buses available.")
            return

        for bus in self.buses:
            print(bus)

        print("=====================================")
