from abc import ABC

class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address

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
        self.menu=FoodItem()

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


mnu=Menu()
item =FoodItem("pizza",12.45,10)
mnu.add_menu_item(item)
mnu.show_menu()

