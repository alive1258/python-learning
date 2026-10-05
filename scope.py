balance=100

def buy_thing(item,price):
    global balance
    balance=balance-price
    print(f"balnce indise the function: {item}", balance)

buy_thing("book", 10)    