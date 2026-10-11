def call():
    print("call someone i dont know")
    return "call done"

class Phone:
    price = 20000
    color = "blue"
    brand = "apple"
    feature =["camera", "specker", "hammer"]

    def call(self):
        print("calling one person")

    def send_sms(self, phone, sms):
        text= f"sending smsm to : {phone} and massaege : {sms}"
        return text    

my_phone = Phone()
print(my_phone.feature)
my_phone.call()    

result= my_phone.send_sms(2343,"miuss u")
print(result)