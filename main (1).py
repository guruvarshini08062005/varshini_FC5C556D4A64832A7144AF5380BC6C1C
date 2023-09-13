class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance:.2f}"

# Example usage:
if __name__ == "__main__":
    # Creating a BankAccount instance
    account = BankAccount("123456", "John Doe", 1000.0)

    # Depositing money
    account.deposit(500.0)

    # Withdrawing money
    account.withdraw(200.0)

    # Displaying the account balance
    print(account.display_balance())