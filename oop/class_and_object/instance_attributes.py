class Shope:
    shoping_maLL ="Jamnuna"
    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[]

    def add_to_cart(self,item):
        self.cart.append(item)

mazan =Shope("me ha")
mazan.add_to_cart("shoe")    
mazan.add_to_cart("phone")  
print(mazan.cart) 

huma =Shope("nisjo ha")
huma.add_to_cart("bakia")    
huma.add_to_cart("yalla")  
print(huma.cart) 

zikka =Shope("zikak ha")
zikka.add_to_cart("hdue")    
zikka.add_to_cart("kdhjd")  
print(zikka.cart)  