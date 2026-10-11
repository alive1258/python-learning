class Bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=100000

    def get_balance(self):
        return self.balance

    def deposit(self,amount):
        if amount >0:
            self.balance +=amount

    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print(f"fokira you can withdraw bellow {self.min_withdraw}")
        elif amount > self.max_withdraw :
            print(f"band forkia haiyua jabye {self.max_withdraw}" ) 
        else:
            self.balance -=amount 
            print(f"her is my money{amount}" )
            print(f"your balce after withdarw : {self.balance}" )
            print(f"your balce after withdarw : {self.get_balance()}" )


back =Bank(15000)
back.withdraw(20)     
back.withdraw(200)     
