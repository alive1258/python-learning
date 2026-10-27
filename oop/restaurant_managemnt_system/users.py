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
      

class Restaurent:
    def __init__(self,name):
        self.name=name
        self.employees=[] #eta database

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

add= Admin("Kamri","1234322","karim@gmail.com","dhaka")
add.add_employee("maruk","123e4322","maruk@gmail.com","dhaka",32,"chef",234565)

add.view_employee()
