'''#Python Decorator
def func1(msg):
    print(msg)
def fun3(str):
    print(str)

fun3("Hii")
func2=fun3
func2("Hello how r u")
f4=func2
f4("99999")'''

'''#Inner function

def function():
    print("This is main function")
    def function_1():
        print("This is function_1")
    def function_2():
        print("This is function_2")

    function_1()
    function_2()

function()'''

'''def add(x):
    return x+1
def sub(x):
    return x-1

def operator(func,x):
    temp=func(x)
    return temp

print(operator(sub,10))
print(operator(add,19))'''


'''def hello():
    def p():
        print("Hello p")
    return p
    
new=hello()
new()'''



'''def divide(x,y):
    print(x/y)
def out_div(func):
    def inner(x,y):
        if(x<y):
            x,y=y,x
            return func(x,y)
    return inner
#divide=out_div(divide)
divide(2,10)

@out_div
def divide(x,y):
    print(x/y)

'''
'''#class Decorator
class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    @property
    def display(self):
        return self.name + "got grade"

stu_=Student("John","B")
print("Name:",stu_.name)
print("Grade:",stu_.grade)
print(stu_.display)'''

#static decorator
class Person:
    @staticmethod
    def hay():
        print("hello peter")

per_=Person()
per_.hay()#static method call using object per_
Person.hay() #static method call using class Person

        
