class BankAccount :
    def __init__(self, account_number, owner, balance=0):
        self.account_number= account_number
        self.owner= owner
        self.balance= balance
        self.transaction_history = []

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f" depositeed ${amount}")
            return f"deposited ${amount}. new balance: ${self.balance}"
        else:
            return "invalid amount"
        
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"withraw ${amount}")
            return f"withdraw ${amount}. new balance: ${self.balance}"
        else:
            return "invalid withdrawal amount"
        
    def get_balance(self):
        return f"current balance: ${self.balance}"
    
    def get_transaction_history(self):
        return self.transaction_history
    


account = BankAccount("12345", "aZIM", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
print(account.transaction_history)
