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