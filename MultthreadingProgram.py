'''import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def _init_(self, threadID, name, q):
          threading.Thread._init_(self)
          self.threadID = threadID
          self.name = name
          self.q = q
    def run(self):
          print("Starting " + self.name)
          process_data(self.name, self.q)
          print("Exiting " + self.name)


def process_data(threadName, q):
   while not exitFlag:
          queueLock.acquire()
          if not workqueue.empty():
              data = q.get()
              queueLock.release()
              print("%s processing %s" % (threadName, data))
          else:
              queueLock.release()
              time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

	# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

	# Fill the queue
   queueLock.acquire()
   for word in nameList:
       workQueue.put(word)
       queueLock.release()

	# Wait for queue to empty
   while not workQueue.empty():
	   pass

	# Notify threads it's time to exit
exitFlag = 1

	# Wait for all threads to complete
for t in threads:
    t.join()
    print("Exiting Main Thread")

import threading
import time

# Function to be run by the threads
def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(f"Letter: {letter}")
        time.sleep(1)
def print_splletters():
    for letter in '@#$&^':
        print(f"Letter: {letter}")
        time.sleep(1)


# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread3 = threading.Thread(target=print_splletters)

# Start threads
thread1.start()
thread2.start()
thread3.start()


# Wait for both threads to finish
thread1.join()
thread2.join()
thread3.join()

print("Both threads have finished.")'''

'''for i in range(1005):
    print(f"Number: {i}",end="")




import threading
import time
def print_numbers():
    for i in range(200):
        print(f"Number: {i}",end="")
        time.sleep(5)

thread1 = threading.Thread(target=print_numbers)
thread1.start()
thread1.join()
print("threads have finished.")'''





import threading
import time

class BankAccount:
    def _init_(self):
        self.balance = 0
        self.lock = threading.Lock()  # Lock to prevent race conditions

    def deposit(self, amount):
        with self.lock:  # Acquire lock
            print(f"Depositing {amount}...")
            time.sleep(1)  # Simulate processing time
            self.balance += amount
            print(f"Deposit completed. Current balance: {self.balance}")

    def withdraw(self, amount):
        with self.lock:  # Acquire lock
            print(f"Withdrawing {amount}...")
            time.sleep(1)  # Simulate processing time
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawal completed. Current balance: {self.balance}")
            else:
                print(f"Insufficient funds. Current balance: {self.balance}")

# Create a shared bank account
account = BankAccount()

# Define tasks
def deposit_task():
    for _ in range(3):
        account.deposit(100)

def withdraw_task():
    for _ in range(2):
        account.withdraw(150)

# Create threads
thread1 = threading.Thread(target=deposit_task)
thread2 = threading.Thread(target=withdraw_task)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print(f"Final balance: {account.balance}")
