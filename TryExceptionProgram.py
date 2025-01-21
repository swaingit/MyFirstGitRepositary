'''try:
    # Code that may raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"The result is {result}")
except ValueError:
    # This block handles invalid input (e.g., entering a non-integer)
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    # This block handles division by zero
    print("Division by zero is not allowed.")
except Exception as e:
    # This block catches any other exception
    print("An unexpected error occurred: {e}")
else:
    # Executes if no exceptions were raised
    print("Operation completed successfully!")
finally:
    # Executes no matter what (exception raised or not)
    print("Program execution finished.")'''
import os
try:
    # Attempt to open and read a file
    file_name = input("Enter the file name: ")
    file_path = os.path.join(os.getcwd(), file_name)
    print("File Path:", file_path)
    with open(file_name, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    # Handle case where the file doesn't exist
    print("Error: The file does not exist.")
except PermissionError:
    # Handle case where the file can't be accessed
    print("Error: You don't have permission to access this file.")
finally:
    # Optional cleanup code
    print("File operation completed.")
