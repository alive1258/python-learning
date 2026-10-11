
class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.cart.append(product)
        print(f"{item} added to cart successfully!")

    def remove_from_cart(self, item_name):
        for item in self.cart:
            if item["item"] == item_name:
                self.cart.remove(item)
                print(f"{item_name} removed from cart successfully!")
                return

        print(f"{item_name} not found in cart!")

    def checkout(self, amount):
        total = 0

        for item in self.cart:
            total += item["price"] * item["quantity"]

        print("Total price:", total)

        if amount < total:
            print(f"Please provide {total - amount} more.")
        else:
            extra = amount - total
            print(f"Purchase successful! Change: {extra}")


swapan = Shopping("Alan Shopan")

swapan.add_to_cart("alu", 50, 6)
swapan.add_to_cart("dim", 80, 3)
swapan.add_to_cart("begin", 30, 4)

print("Before removing:", swapan.cart)

swapan.remove_from_cart("dim")

print("After removing:", swapan.cart)

swapan.checkout(1000)
