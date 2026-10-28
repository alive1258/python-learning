from abc import ABC

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
        print("Total price : {sel.cart.total_price}")    

class Order:
    def __init__(self) -> None:
        self.items={}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] =item.quantity        

    def remove(self):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.items.items())

    def clear(self):
        self.items={}
    

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
      

class Restaurent:
    def __init__(self,name):
        self.name=name
        self.employees=[] #eta database
        self.menu=Menu()

    def add_employee(self,employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee List!")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address) 

    

class Menu:
    def __init__(self):
        self.items =[] # item er db 

    def add_menu_item(self,item):
        self.items.append(item)

    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
            return None

    def remover_item(self,item_name):
        item= self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item deleted")
        else:
            print("item not found") 

    def show_menu(self):
        print("*****Menu*****") 
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")  

class FoodItem:
    def __init__(self,name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity                    

mamr_res=Restaurent("mamaer resturant")
mnu=Menu()
item =FoodItem("pizza",12.45,10)
item2 =FoodItem("eeee",12.45,10)
admin =Admin("abir","abir55@gmail.col",12343,"dhaka")
admin.add_new_item(mamr_res,item)
admin.add_new_item(mamr_res,item2)



customer1 =Customer("abir","abir55@gmail.col",12343,"dhaka")
customer1.view_menu(mamr_res)

