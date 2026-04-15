class BankAccount:
    def __init__(self, deposit, balance):
        self.deposit = deposit
        self.__balance = balance # Private
        
    def get_balance(self):
        return self.__balance
    
    def deposit(self):
        amount = float(input("Enter amount: "))
        self.__balance += amount
        print("\nAmount Deposited:", amount)
        
        
    