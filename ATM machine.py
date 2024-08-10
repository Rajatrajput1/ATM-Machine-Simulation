# ATM Machine Simulation with Choices

class ATMMachine:
    def __init__(self, initial_balance=0):
        # Initialize the ATM with an initial balance and default PIN
        self.balance = initial_balance
        self.pin = "1234"  # Default PIN
        self.transaction_history = []

    def check_balance(self):
        # Return the current account balance
        return f"Your current balance is: ${self.balance}"

    def withdraw_cash(self, amount):
        # Withdraw a specified amount of cash from the account
        if amount > self.balance:
            return "Insufficient balance!"
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw: ${amount}")
            return f"${amount} withdrawn successfully!"

    def deposit_cash(self, amount):
        # Deposit a specified amount of cash into the account
        self.balance += amount
        self.transaction_history.append(f"Deposit: ${amount}")
        return f"${amount} deposited successfully!"

    def change_pin(self, old_pin, new_pin):
        # Change the PIN if the old PIN is correct
        if self.pin == old_pin:
            self.pin = new_pin
            return "PIN changed successfully!"
        else:
            return "Incorrect old PIN!"

    def show_transaction_history(self):
        # Return the transaction history
        return self.transaction_history if self.transaction_history else "No transactions yet."

def main():
    atm = ATMMachine(initial_balance=1000)

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. Show Transaction History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print(atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw_cash(amount))
        elif choice == '3':
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit_cash(amount))
        elif choice == '4':
            old_pin = input("Enter old PIN: ")
            new_pin = input("Enter new PIN: ")
            print(atm.change_pin(old_pin, new_pin))
        elif choice == '5':
            print("Transaction History:")
            for transaction in atm.show_transaction_history():
                print(transaction)
        elif choice == '6':
            print("Exiting... Have a nice day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
