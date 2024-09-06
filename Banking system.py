logo = """

|¯¯¯|         /¯¯¯¯¯| |¯¯¯\|¯¯¯| |¯¯¯|/¯¯¯/    O    |¯¯¯\|¯¯¯|  /¯¯¯¯¯\' 
|      ¯¯\'  /     !     | |            '|||          <° |¯¯¯¯| |            '|||   (/¯¯¯\°
|__x__/°/___/¯|__'| |___|\___| |___|\___\ |____| |___|\___|  \_____/' 

"""
print(logo)

import random
import time

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f} into account {self.account_number}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_number}. New balance: ${self.balance:.2f}")

    def transfer(self, recipient, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            recipient.balance += amount
            print(f"Transferred ${amount:.2f} from account {self.account_number} to account {recipient.account_number}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder):
        account_number = random.randint(10000000, 99999999)
        self.accounts[account_number] = BankAccount(account_number, account_holder)
        print(f"Account created for {account_holder} with account number {account_number}")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def list_accounts(self):
        for account_number, account in self.accounts.items():
            print(f"Account {account_number}: {account.account_holder} - ${account.balance:.2f}")

def main():
    bank = Bank()

    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. List Accounts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_holder = input("Enter your name: ")
            bank.create_account(account_holder)
        elif choice == "2":
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter amount to deposit: "))
            account = bank.get_account(account_number)
            if account:
                account.deposit(amount)
            else:
                print("Account not found!")
        elif choice == "3":
            account_number = int(input("Enter your account number: "))
            amount = float(input("Enter amount to withdraw: "))
            account = bank.get_account(account_number)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found!")
        elif choice == "4":
            sender_account_number = int(input("Enter your account number: "))
            recipient_account_number = int(input("Enter recipient's account number: "))
            amount = float(input("Enter amount to transfer: "))
            sender_account = bank.get_account(sender_account_number)
            recipient_account = bank.get_account(recipient_account_number)
            if sender_account and recipient_account:
                sender_account.transfer(recipient_account, amount)
            else:
                print("Account not found!")
        elif choice == "5":
            bank.list_accounts()
        elif choice == "6":
            print("Exiting...")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()












