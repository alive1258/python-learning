from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address

class Customer(User):
    def __init__(self, name, phone, email, address):
            super().__init__(name, phone, email, address)
            self.cart=Order()

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self,restaurent,item_name,quantity):
        item=restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("item quantity exceeded")
            else:
                item.quantity=quantity
                self.cart.add_item(item)
                print("item Added")
        else:
            print("item not found")

    def view_cart(self):
        print("*****View Cart*****") 
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")  
        print(f"Total price : {self.cart.total_price}")   

def pay_bill(self):
    print(f"total {self.cart.total_price} paid successfully")
    self.clear()

class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age=age
        self.designation=designation
        self.salary=salary

# emp= Employee("rayhan","rayhan99@gmail.com",234422,"dhaka",22,"chef",120000)
# print(emp.name)

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
       

    def add_employee(self,restaurent,employee):
        restaurent.add_employee(employee)

    def view_employee(self,restaurent):
        restaurent.view_employee ()

    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu_item(item)

    def delete_item(self,restaurent,item):
        restaurent.menu.remover_item(item)  

    def view_items(self,restaurent):
        restaurent.menu.show_menu()   



    


      





               



