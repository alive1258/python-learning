class Phone:
    manufactured ="China"

    def __init__(self,owner,band,price):
        self.owner = owner
        self.brand = band
        self.price = price

    def send_smd(self,phone,sms):
        text=f"sending sms to : {phone} and send {sms}"
        print(text)

my_phone = Phone("miraj","apple",9800)
print(my_phone.price,my_phone.owner,my_phone.brand)

her_phone = Phone("Amina","Smasong",8800)
print(her_phone.price,her_phone.owner,her_phone.brand)

