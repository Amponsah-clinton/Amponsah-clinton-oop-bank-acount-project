class account:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, deposit):
        self.__deposit = deposit
        self.__balance = self.__deposit + self.__balance 
        return self.__balance 
    def withdraw(self, amount):
        self.__withdraw = amount
        if self.__balance <= amount:
            print("ERROR : Insufficient balance")
        else:
            self.__balance = self.__balance - amount
        return self.__balance

account1 = account(100)
print(account1.deposit(200))

print(account1.withdraw(10))

         