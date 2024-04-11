class BankAccount():
    def __init__(self, account_num, initial_balance=0):
        self.__balance = initial_balance
        self.__account_num = account_num

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid amount for deposit.")

    def withdrawal(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid amount for withdrawal or insufficient funds.")

    def balance_inquiry(self):
        print(f"Account Number: {self.__account_num}, Balance: ${self.__balance}")


# Example usage:
account = BankAccount(10990, 1000)
account.deposit(500)
account.withdrawal(200)
account.balance_inquiry()
