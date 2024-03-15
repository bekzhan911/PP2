class Account:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f} tenge. New balance: {self.balance:.2f} tenge")
        else:
            print("Invalid deposit amount. Please deposit a positive value.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount:.2f} tenge. New balance: {self.balance:.2f} tenge")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

# Example usage
account1 = Account("Bakytbergen", 1000)
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(1500)  # This should print an error message
account1.deposit(-100)  # This should print an error message
