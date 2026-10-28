
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


if __name__ == "__main__":
    customer_menu()
