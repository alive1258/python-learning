def full_name(fist,last):
    name = fist + " " + last
    return name

name = full_name("John", "Doe")
print("Full name:", name)

def famous_name(fist,last,title,adition):
    name = title + " " + fist + " " + last + " " + adition
    return name
name = famous_name("John", "Doe", "Mr.", "PhD")
print("Famous name:", name)

def a_lot(num1,num2):
    total = num1 + num2
    multiplication = num1 * num2
    remainder = num1 % num2
    return total, multiplication, remainder
print("Total, Multiplication, Remainder:", a_lot(10, 3))