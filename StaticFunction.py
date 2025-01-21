class MyClass:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Static method
    @staticmethod
    def greet():
        return "Hello, welcome to MyClass!"

    # Instance method
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

# Create an instance of MyClass
person = MyClass("Alice", 30)

# Call the static method
print(MyClass.greet())

# Call the instance method
print(person.display_info())
