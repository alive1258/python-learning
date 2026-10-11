try:
    with open("data.txt", "r") as file:
        data = file.read()

    print(data)

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

finally:
    print("Done.")

#Read
try:
    with open("data.txt", "r") as file:
        data = file.read()

    print(data)

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

finally:
    print("Read operation completed.")


#Write
try:
    with open("data.txt", "w") as file:
        file.write("Hello Python\n")
        file.write("Learning file handling\n")

except PermissionError:
    print("Permission denied.")

finally:
    print("Write operation completed.")

#Append
try:
    with open("data.txt", "a") as file:
        file.write("New line added\n")

except PermissionError:
    print("Permission denied.")

finally:
    print("Append operation completed.")