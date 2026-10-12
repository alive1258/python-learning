
class Employee:
    """Base class for company employees."""

    def __init__(self, name, age, phone, salary):
        self.name = name
        self.age = age
        self.phone = phone
        self.salary = salary

    def show_info(self):
        return (
            f"Name: {self.name}, Age: {self.age}, "
            f"Phone: {self.phone}, Salary: {self.salary}"
        )


class Driver(Employee):
    """Driver inherits common employee information."""

    def __init__(self, name, age, phone, salary, license_number):
        super().__init__(name, age, phone, salary)
        self.license_number = license_number

    def show_info(self):
        return (
            f"{super().show_info()}, "
            f"License: {self.license_number}"
        )


class Counter(Employee):
    """Employee who manages ticket sales."""

    def __init__(self, name, age, phone, salary, counter_id):
        super().__init__(name, age, phone, salary)
        self.counter_id = counter_id


class Manager(Employee):
    """Manages company operations."""

    def __init__(self, name, age, phone, salary, department):
        super().__init__(name, age, phone, salary)
        self.department = department


class Supervisor(Employee):
    """Supervises drivers, buses, or routes."""

    def __init__(self, name, age, phone, salary, assigned_area):
        super().__init__(name, age, phone, salary)
        self.assigned_area = assigned_area


class Passenger:
    """Represents a passenger."""

    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def show_info(self):
        return (
            f"Passenger: {self.name}, "
            f"Age: {self.age}, Phone: {self.phone}"
        )


class Route:
    """Represents a bus route."""

    def __init__(self, route_id, start, destination, fare):
        self.route_id = route_id
        self.start = start
        self.destination = destination
        self.fare = fare

    def show_info(self):
        return (
            f"Route {self.route_id}: {self.start} -> "
            f"{self.destination}, Fare: {self.fare} BDT"
        )


class Bus:
    """Represents a bus in the fleet."""

    def __init__(self, bus_number, capacity):
        self.bus_number = bus_number
        self.__capacity = capacity  # Private attribute
        self.__passengers = []
        self.driver = None
        self.route = None

    @property
    def capacity(self):
        return self.__capacity

    @property
    def passengers(self):
        return tuple(self.__passengers)

    def assign_driver(self, driver):
        if not isinstance(driver, Driver):
            raise TypeError("A valid Driver object is required.")

        self.driver = driver
        print(f"Driver {driver.name} assigned to {self.bus_number}")

    def assign_route(self, route):
        if not isinstance(route, Route):
            raise TypeError("A valid Route object is required.")

        self.route = route
        print(f"Route {route.route_id} assigned to {self.bus_number}")

    def book_seat(self, passenger):
        if not isinstance(passenger, Passenger):
            raise TypeError("A valid Passenger object is required.")

        if len(self.__passengers) >= self.__capacity:
            print(f"Sorry! Bus {self.bus_number} is full.")
            return False

        self.__passengers.append(passenger)
        print(
            f"Seat booked for {passenger.name} "
            f"on bus {self.bus_number}"
        )
        return True

    def show_info(self):
        driver_name = self.driver.name if self.driver else "Not assigned"
        route_name = (
            f"{self.route.start} -> {self.route.destination}"
            if self.route else "Not assigned"
        )

        return (
            f"Bus: {self.bus_number}, "
            f"Capacity: {self.__capacity}, "
            f"Passengers: {len(self.__passengers)}, "
            f"Driver: {driver_name}, Route: {route_name}"
        )


class Company:
    """Manages all fleet operations."""

    def __init__(self, name, address):
        self.name = name
        self.address = address

        self.buses = []
        self.routes = []
        self.drivers = []
        self.counters = []
        self.managers = []
        self.supervisors = []
        self.passengers = []

    def add_bus(self, bus):
        if not isinstance(bus, Bus):
            raise TypeError("A valid Bus object is required.")

        if any(b.bus_number == bus.bus_number for b in self.buses):
            print("This bus is already registered.")
            return False

        self.buses.append(bus)
        print(f"Bus {bus.bus_number} registered successfully.")
        return True

    def add_route(self, route):
        if not isinstance(route, Route):
            raise TypeError("A valid Route object is required.")

        self.routes.append(route)
        print(f"Route {route.route_id} added successfully.")
        return True

    def add_driver(self, driver):
        if not isinstance(driver, Driver):
            raise TypeError("A valid Driver object is required.")

        self.drivers.append(driver)
        print(f"Driver {driver.name} registered successfully.")
        return True

    def add_counter(self, counter):
        if not isinstance(counter, Counter):
            raise TypeError("A valid Counter object is required.")

        self.counters.append(counter)
        return True

    def add_manager(self, manager):
        if not isinstance(manager, Manager):
            raise TypeError("A valid Manager object is required.")

        self.managers.append(manager)
        return True

    def add_supervisor(self, supervisor):
        if not isinstance(supervisor, Supervisor):
            raise TypeError("A valid Supervisor object is required.")

        self.supervisors.append(supervisor)
        return True

    def register_passenger(self, passenger):
        if not isinstance(passenger, Passenger):
            raise TypeError("A valid Passenger object is required.")

        self.passengers.append(passenger)
        print(f"Passenger {passenger.name} registered successfully.")
        return True

    def show_company_info(self):
        print("\n========== COMPANY INFORMATION ==========")
        print(f"Company: {self.name}")
        print(f"Address: {self.address}")
        print(f"Total buses: {len(self.buses)}")
        print(f"Total routes: {len(self.routes)}")
        print(f"Total drivers: {len(self.drivers)}")
        print(f"Total counters: {len(self.counters)}")
        print(f"Total managers: {len(self.managers)}")
        print(f"Total supervisors: {len(self.supervisors)}")
        print(f"Total passengers: {len(self.passengers)}")

    def show_fleet(self):
        print("\n========== FLEET DETAILS ==========")

        if not self.buses:
            print("No buses registered.")
            return

        for bus in self.buses:
            print(bus.show_info())


# ==========================================
# Example: Using the Fleet Management System
# ==========================================

company = Company("Green Line Transport", "Dhaka, Bangladesh")

# Create employees
driver1 = Driver(
    "Rahim", 35, "01711111111", 30000, "DL-1001"
)

counter1 = Counter(
    "Karim", 28, "01722222222", 18000, "CNT-01"
)

manager1 = Manager(
    "Hasan", 40, "01733333333", 50000, "Operations"
)

supervisor1 = Supervisor(
    "Jamal", 32, "01744444444", 25000, "Dhaka Region"
)

# Create route, bus, and passenger
route1 = Route("R-101", "Dhaka", "Rajshahi", 700)
bus1 = Bus("BUS-001", 2)

passenger1 = Passenger("Sakib", 24, "01755555555")
passenger2 = Passenger("Nila", 22, "01766666666")
passenger3 = Passenger("Mina", 25, "01777777777")

# Register everything with the company
company.add_driver(driver1)
company.add_counter(counter1)
company.add_manager(manager1)
company.add_supervisor(supervisor1)

company.add_route(route1)
company.add_bus(bus1)

company.register_passenger(passenger1)
company.register_passenger(passenger2)

# Assign driver and route
bus1.assign_driver(driver1)
bus1.assign_route(route1)

# Book seats
bus1.book_seat(passenger1)
bus1.book_seat(passenger2)
bus1.book_seat(passenger3)  # Bus is full

# Display details
company.show_company_info()
company.show_fleet()

print("\n========== DRIVER INFORMATION ==========")
print(driver1.show_info())

print("\n========== ROUTE INFORMATION ==========")
print(route1.show_info())
