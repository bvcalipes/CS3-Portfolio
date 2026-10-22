class BankAccount:
    def __init__(self, account_number: int, balance:float):
        self.account_number = account_number
        self.balance = balance
    
    def set_account_number(self, account_number: int):
        self.__account_number = account_number
        self.set_account_number(account_number)

    def set_balance(self, balance: float):
        self.__balance = balance
        if balance < 0:
            return "The balance must not be a negative number."
        
    def get_account_number(self):
        return f"Account Number: {self.account_number}"

    def get_balance(self):
        return f"Balance: {self.balance:.2f}"

a1 = BankAccount (123456, 1000.00) #Object for the bank account
print("Account 1")
print(a1.get_account_number())
print("Balance:", a1.get_balance())
print()
print("\nUpdate balance to -100")
print(a1.set_balance(-100))
print(a1.get_account_number())
print("Balance:", a1.get_balance())