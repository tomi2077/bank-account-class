class BankAccount:
    total_accounts = 0

    def __init__(self, account_holder, balance = 0 ):
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.total_accounts += 1 
    
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient FUnds")

    def get_balance(self):
        return self.balance
    
    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts


account_1 = BankAccount("Josh", 20)
account_2 = BankAccount("Sarah", 50)
account_3 = BankAccount("John") 

account_1.deposit(30)
print(f"{account_1.account_holder}'s balance: ${account_1.get_balance()}")

account_2.withdraw(20)
print(f"{account_2.account_holder}'s balance: ${account_2.get_balance()}")  

account_3.withdraw(20)
print(f"{account_3.account_holder}'s balance: ${account_3.get_balance()}")  

# Check total accounts
print(f"Total accounts created: {BankAccount.get_total_accounts()}")
