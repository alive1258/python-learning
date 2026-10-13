class Bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name=holder_name
        self.branch="dhaka"
        self.__balance=initial_deposit

    def deposit(self,amount):
        self.__balance   +=amount 

    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance = self.__balance -amount
            return amount 
        else:
            return f"fokira balance nai"

    def get_balance(self):
        return  self.__balance 

rafsan =Bank("choto vai",10000)

print(rafsan.holder_name)
print(rafsan.__balance) 
rafsan.deposit(40000)
print(rafsan.get_balance()) 
print(rafsan.branch) 
print(dir(rafsan))