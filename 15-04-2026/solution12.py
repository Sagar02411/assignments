# Q12 (Medium) – Encapsulation
class BankAccount:
    def __init__(self):
        self.__balance = 1000

    def deposit(self,amount):
        self.__balance += amount
        return self.__balance

    def get_balance(self):
        return self.__balance
    
r1 = BankAccount()
r1.deposit(100)
print (r1.get_balance())