import threading

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:  # Acquire lock
            self.balance += amount
            print(f"Deposited {amount}, new balance: {self.balance}")

    def withdraw(self, amount):
        with self.lock:  # Acquire lock
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}, new balance: {self.balance}")
            else:
                print(f"Insufficient funds for withdrawal of {amount}")

if __name__ == "__main__":
    account = BankAccount()

    # Create two threads for deposit and withdrawal
    t1 = threading.Thread(target=account.deposit(100))
    t2 = threading.Thread(target=account.withdraw(150))

    # Start the threads
    t1.start()
    t2.start()

    # Wait for the threads to finish
    t1.join()
    t2.join()

    # Print the final balance
    print(f"Final balance: {account.balance}")
