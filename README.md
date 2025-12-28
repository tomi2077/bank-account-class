# Bank Account Class Written in Python

## Overview
This repository contains a simple Python banking class that models basic banking operations such as account creation, deposits, withdrawals, and balance inquiries.

## Features
- Bank account creation with account holder name and initial balance
- Money depositing
- Money withdrawal with balance validation
- Account balance checking
- Total number of accounts tracking using class methods

## Project Structure
```
bank-account-class/
├── src/
│   └── bankaccount.py
├── README.md
└── .gitignore
```

## Requirements
- Python 3.14 or higher

## Installation
1. Clone this repository:
```bash
   git clone https://github.com/tomi2077/bank-account-class.git
```
2. Navigate to the project directory:
```bash
   cd bank-account-class
```

## Usage
```python
from src.bankaccount import BankAccount

# Create bank accounts
account1 = BankAccount("Josh", 100)
account2 = BankAccount("Sarah", 50)

# Deposit money
account1.deposit(50)

# Withdraw money
account1.withdraw(30)

# Check balance
print(account1.get_balance())

# Check total accounts created
print(BankAccount.get_total_accounts())
```

## Future Improvements
- Add transaction history tracking
- Implement interest calculation
- Add unit tests with pytest
- Add account number generation
- Implement account authentication