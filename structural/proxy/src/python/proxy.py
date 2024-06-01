
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def get_balance(self):
        return self.balance


class BankAccountProxy:
    def __init__(self, owner, balance=0):
        self.bank_account = BankAccount(owner, balance)
        self.permissions = {"view_balance": False, "modify_balance": False}

    def set_permissions(self, view_balance=False, modify_balance=False):
        self.permissions["view_balance"] = view_balance
        self.permissions["modify_balance"] = modify_balance

    def deposit(self, amount):
        if self.permissions["modify_balance"]:
            self.bank_account.deposit(amount)
        else:
            print("Permission denied: Cannot deposit")

    def withdraw(self, amount):
        if self.permissions["modify_balance"]:
            self.bank_account.withdraw(amount)
        else:
            print("Permission denied: Cannot withdraw")

    def get_balance(self):
        if self.permissions["view_balance"]:
            return self.bank_account.get_balance()
        else:
            print("Permission denied: Cannot view balance")
            return None

def main():
    # Example usage
    proxy = BankAccountProxy("Alice", 100)
    proxy.set_permissions(view_balance=True, modify_balance=False)

    # Trying to view the balance
    print(f"Balance: ${proxy.get_balance()}")

    # Trying to deposit money
    proxy.deposit(50)

    # Trying to withdraw money
    proxy.withdraw(30)

    # Update permissions to allow modifying balance
    proxy.set_permissions(view_balance=True, modify_balance=True)

    # Trying to deposit money again
    proxy.deposit(50)

    # Trying to withdraw money again
    proxy.withdraw(30)

    # Viewing the balance after transactions
    print(f"Balance: ${proxy.get_balance()}")

if __name__ == "__main__":
    main()


"""
Scenario:

We have a BankAccount class that represents a user's bank account. We will create a 
BankAccountProxy class that controls access to the BankAccount class. The proxy will 
check if the user has the right permissions before allowing access to the account's 
balance.
"""