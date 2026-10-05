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