import threading
import time

# Function to calculate squares
def calculate_squares(numbers):
    for n in numbers:
        time.sleep(0.5)  # Simulate computation
        print(f"Square of {n}: {n * n}--")

# Function to calculate cubes
def calculate_cubes(numbers):
    for n in numbers:
        time.sleep(0.5)  # Simulate computation
        print(f"--Cube of {n}: {n * n * n}")

# List of numbers
numbers = [2,3,4,5,6]

# Create threads
thread1 = threading.Thread(target=calculate_squares, args=(numbers,))
thread2 = threading.Thread(target=calculate_cubes, args=(numbers,))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Finished calculating squares and cubes.")
