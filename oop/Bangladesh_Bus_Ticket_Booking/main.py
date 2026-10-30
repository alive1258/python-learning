
from bus_system import BusSystem
from admin import Admin


# Create objects
bus_system = BusSystem()
admin = Admin()


# Add some demo buses
bus_system.admin_logged_in = True

bus_system.add_bus("B101", "Dhaka - Sirajganj", 40)
bus_system.add_bus("B102", "Dhaka - Rajshahi", 35)
bus_system.add_bus("B103", "Dhaka - Chittagong", 45)

bus_system.admin_logged_in = False


# Admin menu
def admin_menu():
    while bus_system.admin_logged_in:

        print("\n========== ADMIN MENU ==========")
        print("1. Add Bus")
        print("2. View All Buses")
        print("3. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            number = input("Enter Bus Number: ").strip()
            route = input("Enter Bus Route: ").strip()

            try:
                seats = int(input("Enter Total Seats: "))
                message = bus_system.add_bus(number, route, seats)
                print(message)

            except ValueError:
                print("Invalid seats! Please enter a number.")

        elif choice == "2":
            bus_system.show_buses()

        elif choice == "3":
            bus_system.admin_logged_in = False
            print("Admin logged out successfully!")

        else:
            print("Invalid choice! Please try again.")


# Admin login
def admin_login():
    print("\n========== ADMIN LOGIN ==========")

    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()

    if admin.login(username, password):
        bus_system.admin_logged_in = True
        print("Login successful!")

        admin_menu()

    else:
        print("Invalid username or password!")


# Book ticket
def book_ticket():
    print("\n========== BOOK TICKET ==========")

    bus_system.show_buses()

    bus_number = input("Enter Bus Number: ").strip()
    name = input("Enter Passenger Name: ").strip()
    phone = input("Enter Phone Number: ").strip()

    passenger, message = bus_system.book_ticket(
        bus_number,
        name,
        phone
    )

    print(message)

    if passenger:
        passenger.show_ticket()


# Main user menu
def main_menu():
    while True:

        print("\n====== BANGLADESH BUS TICKET BOOKING ======")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            admin_login()

        elif choice == "2":
            book_ticket()

        elif choice == "3":
            bus_system.show_buses()

        elif choice == "4":
            print("Thank you for using our Bus Ticket Booking System!")
            break

        else:
            print("Invalid choice! Please select 1-4.")


# Start application
if __name__ == "__main__":
    main_menu()
