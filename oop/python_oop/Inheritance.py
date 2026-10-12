#base class, parent calss,common attribute+ funtionality call
# derived call, child class,,uncommon attribute _funtionality calls

class Device:
    def __init__(self, brand, price, color,origin) -> None:
            self.brand = brand
            self.price = price
            self.color = color
            self.origin = origin

    def run(self):
        return f"Running Latop : {self.brand}"        
         

class Laptop:
    def __init__(self, memory) -> None:
      
        self.memory = memory

    def show_info(self):
        return (
          
            f"Color: {self.color}, Memory: {self.memory}"
        )





class Phone(Device):
    def __init__(self,  dual_sim,brand, price, color,origin) -> None:
       
        self.dual_sim = dual_sim
        super().__init__(brand, price, color,origin)

    def send_sms(self, number, text):
        return f"Sending SMS to {number}: {text}"

    def __repr__(self) ->str:
        return f"Phone : {self.price} {self.dual_sim} {self.color}"



    
class Camera:
    def __init__(self, megapixels) -> None:
     
        self.megapixels = megapixels


    def show_info(self):
        return (
         
            f"Color: {self.color}, Megapixels: {self.megapixels}MP"
        )

# inheritance
my_phone= Phone("iphobe",1200,"silver","china" ,True)
print(my_phone.brand)
print(my_phone)


