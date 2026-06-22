class MobileMoney:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        print(f"Deposited UGX {amount:,.2f}. New balance: UGX {self.balance:,.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:
            print(f"Insufficient funds. Current balance is UGX {self.balance:,.2f}")
            return
        self.balance -= amount
        print(f"Withdrew UGX {amount:,.2f}. New balance: UGX {self.balance:,.2f}")

    def check_balance(self):
        print(f"Current balance: UGX {self.balance:,.2f}")
        return self.balance


# --- Testing the application ---
account = MobileMoney(50000)   # start with an initial balance

print("--- Initial Balance ---")
account.check_balance()

print("\n--- After Deposit ---")
account.deposit(20000)
account.check_balance()

print("\n--- After Withdraw ---")
account.withdraw(30000)
account.check_balance()   # this line confirms the balance updated correctly after withdrawal