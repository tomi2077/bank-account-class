from src.bankaccount import BankAccount

# Create bank accounts
account1 = BankAccount("Joshua", 100)
account2 = BankAccount("Sarah", 50)

# Deposit money
account1.deposit(50)
print(f"{account1.account_holder}'s balance: ${account1.get_balance()}")

# Withdraw money
account1.withdraw(30)
print(f"After withdrawal: ${account1.get_balance()}")

# Check total accounts
print(f"Total accounts: {BankAccount.get_total_accounts()}")