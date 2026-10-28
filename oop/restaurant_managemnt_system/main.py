
from food_item import FoodItem
from menu import Menu
from users import Customer, Admin, Employee
from restaurent import Restaurent
from orders import Order

mamer_restaurant = Restaurent("Mamer Restaurant")
def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")

    customer = Customer(
        name=name,
        email=email,
        phone=phone,
        address=address
    )

    # Customer menu
    while True:
        print(f"\nWelcome, {customer.name}!")
        print("\n--- Customer Menu ---")
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            customer.view_menu(mamer_restaurant)
     
        elif choice == 2:
            item_name = int(input("Enter item name : "))
            item_quantity = int(input("Enter item quantity : "))
            customer.add_to_cart(mamer_restaurant, item_name,item_quantity)
            

        elif choice == 3:
            customer.view_cart()

        elif choice == 4:
            customer.pay_bill()

        elif choice == 5:
            print(f"Goodbye, {customer.name}!")
            break

        else:
            print("Invalid choice! Please try again.")


def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")

    admin = Admin(
        name=name,
        email=email,
        phone=phone,
        address=address
    )

    # admin menu
    while True:
        print(f"\nWelcome, {admin.name}!")
        print("\n--- admin Menu ---")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View items")
        print("5. Delete Item")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Assumes your Admin class has this method.
            item_name = input("Enter item name: ")
            item_price = float(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            item = FoodItem(item_name, item_price,item_quantity)
            admin.add_new_item(mamer_restaurant, item)

        elif choice == 2:
            employee_name = input("Enter employee name: ")
            employee_email = input("Enter employee email: ")
            employee_phone = input("Enter employee phone: ")
            employee_address = input("Enter employee address: ")
            employee_age = input("Enter employee age: ")
            employee_designation = input("Enter employee designation: ")
            employee_salary = input("Enter employee salary: ")

            employee = Employee(
                name=employee_name,
                email=employee_email,
                phone=employee_phone,
                address=employee_address,
                age=employee_age,
                designation=employee_designation,
                salary=employee_salary
            )

            admin.add_employee(mamer_restaurant, employee)

        elif choice == 3:
            admin.view_employees(mamer_restaurant)

        elif choice == 4:
            admin.view_items(mamer_restaurant)

        elif choice == 5:
            item_name = input("Enter item name to delete: ")
            admin.remove_item(mamer_restaurant, item_name)

        elif choice == 6:
            print(f"Goodbye, {admin.name}!")
            break

        else:
            print("Invalid choice! Please select 1-6.")
