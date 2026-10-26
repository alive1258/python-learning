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
        self.employees=[] #eta database

    def add_employee(self,name,email,phone,address,age,designation,salary):
        # employee class er ekta object make hoya jaby
        employee=Employee(name,email,phone,address,age,designation,salary)  
        self.employees.append(employee)
        print(f"{name} is added!") 

    def view_employee(self):
        print("Employee List!")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)    
      


add= Admin("Kamri","1234322","karim@gmail.com","dhaka")
add.add_employee("maruk","123e4322","maruk@gmail.com","dhaka",32,"chef",234565)

add.view_employee()
