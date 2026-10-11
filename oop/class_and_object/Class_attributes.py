class Shope:
    cart =[] #class atribute
    def __init__(self,buyer):
        self.buyer=buyer

    def add_to_cart(self,item):
        self.cart.append(item)

mazan =Shope("me ha")
mazan.add_to_cart("shoe")    
mazan.add_to_cart("phone")  
print(mazan.cart) 

huma =Shope("me ha")
huma.add_to_cart("bakia")    
huma.add_to_cart("yalla")  
print(huma.cart)  