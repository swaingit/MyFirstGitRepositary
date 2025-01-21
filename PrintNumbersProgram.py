import threading
import time

# Define a function for the thread
def print_numbers(name, count):
    for i in range(1, count + 1):
        print(f"Thread {name}: {i}")
        time.sleep(0.5)  # Simulate some work

# Create threads
thread1 = threading.Thread(target=print_numbers, args=("A", 5))
thread2 = threading.Thread(target=print_numbers, args=("B", 5))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("All threads have finished execution.")
