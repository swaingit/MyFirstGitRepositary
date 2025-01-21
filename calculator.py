'''class Calculator:
    # A simple class with static methods
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

# Access the methods without creating an instance
result1 = Calculator.add(5, 3)
result2 = Calculator.subtract(10, 4)

print("Addition:", result1)      # Output: Addition: 8
print("Subtraction:", result2)   # Output: Subtraction: 6'''

'''class Greetings:
    # A class method that doesn't use self or init
    def say_hello():
        return "Hello, world!"

    def say_goodbye():
        return "Goodbye, see you soon!"

# Access the methods directly from the class
print(Greetings.say_hello())   # Output: Hello, world!
print(Greetings.say_goodbye()) # Output: Goodbye, see you soon!'''

'''class Animal:
    # Method to set attributes
    def set_attributes(self, name, sound):
        self.name = name
        self.sound = sound

    # Method to display the animal's information
    def make_sound(self):
        print(f"The {self.name} goes '{self.sound}'.")

# Create an object of the class
dog = Animal()

# Set attributes using the method
Animal.set_attributes(dog, "Dog", "Woof")

# Call a method using the object
Animal.make_sound(dog)'''
class Car:
    # Method to set car details
    def set_details(car_object, brand, model):
        car_object.brand = brand
        car_object.model = model

    # Method to display car details
    def show_details(car_object):
        print(f"This car is a {car_object.brand} {car_object.model}.")

# Create an object of the class
my_car_obj = Car()

# Set attributes using a method
Car.set_details(class Car:
    # Method to set car details
    def set_details(car_object, brand, model):
        car_object.brand = brand
        car_object.model = model

    # Method to display car details
    def show_details(car_object):
        print(f"This car is a {car_object.brand} {car_object.model}.")

# Create an object of the class
my_car = Car()

# Set attributes using a method
Car.set_details(my_car, "Toyota", "Corolla")

# Call a method using the object
Car.show_details(my_car), "Toyota", "Corolla")

# Call a method using the object
Car.show_details(my_car_obj)
