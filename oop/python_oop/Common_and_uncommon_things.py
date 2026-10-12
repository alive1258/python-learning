
class Laptop:
    def __init__(self, brand, price, color, memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def show_info(self):
        return (
            f"Brand: {self.brand}, Price: {self.price}, "
            f"Color: {self.color}, Memory: {self.memory}"
        )


my_laptop = Laptop("HP", 65000, "Silver", "16GB")
print(my_laptop.show_info())


class Phone:
    def __init__(self, brand, price, color, dual_sim) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim

    def phone_call(self, number):
        return f"Calling {number} from my {self.brand} phone."

    def send_sms(self, number, text):
        return f"Sending SMS to {number}: {text}"

    def show_info(self):
        return (
            f"Brand: {self.brand}, Price: {self.price}, "
            f"Color: {self.color}, Dual SIM: {self.dual_sim}"
        )

    
class Camera:
    def __init__(self, brand, price, color, megapixels) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.megapixels = megapixels

    def take_photo(self, subject):
        return f"Taking a photo of {subject} with my {self.brand} camera."

    def record_video(self, duration):
        return f"Recording a {duration}-minute video with my {self.brand} camera."

    def show_info(self):
        return (
            f"Brand: {self.brand}, Price: {self.price}, "
            f"Color: {self.color}, Megapixels: {self.megapixels}MP"
        )


# Create an object
my_camera = Camera("Canon", 55000, "Black", 24)

# Access object attributes
print(my_camera.brand)
print(my_camera.price)
print(my_camera.color)
print(my_camera.megapixels)

# Call methods
print(my_camera.take_photo("Nature"))
print(my_camera.record_video(5))
print(my_camera.show_info())



# Create a Phone object
my_phone = Phone("Samsung", 25000, "Black", True)

# Access attributes
print(my_phone.brand)
print(my_phone.price)
print(my_phone.color)
print(my_phone.dual_sim)

# Call methods
print(my_phone.phone_call("01712345678"))
print(my_phone.send_sms("01712345678", "Hello! How are you?"))
print(my_phone.show_info())
