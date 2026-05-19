class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _get_balance(self):
        print(f"Balance: {self.balance}")  #Protected

    def __update_balance(self, amount):
        self.balance += amount             #privae

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)  #private
            self._get_balance()           #protected 
        else:
            print("Invalid deposit amount!")
            
account = BankAccount()
account._get_balance()      
# account.deposit(500)         
