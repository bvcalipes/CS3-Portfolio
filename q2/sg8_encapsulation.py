class BankAccount:
    def __init__(self, account_number: int, balance:float):
        self.account_number = account_number
        self.balance = balance
    
    def set_account_number(self, account_number: int):
        self.__account_number = account_number
        self.set_account_number(account_number)

    def set_balance(self, balance: float):
        self.__balance = balance
        self.set_balance(balance)
        
    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance
    
a1 = BankAccount(123456, 1000.00) #Object for the bank account
print("Account 1")
print("Account Number:", a1.get_account_number())
print("Balance:", a1.get_balance())
