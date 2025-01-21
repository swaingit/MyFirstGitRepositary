'''def funct(n):
    return lambda x:x*n
result=funct(2)
print("Double the number of 15=",result(5))
result=funct(3)
print("Double the number of 15=",result(15))
result=funct(4)
print("Double the number of 15=",result(15))
result=funct(5)'''



'''nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nSquare every number of the said list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
print("\nCube every number of the said list:")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)'''

'''starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Python'))
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Java'))'''

'''t="pmango"
p=lambda b: True if t.startswith('m') else False
print(p(t))'''

'''import datetime
current_time=datetime.datetime.now()
print(current_time)
y=lambda x:x.year
print(y(current_time))
m=lambda x:x.month
print(m(current_time))
d=lambda x:x.day
print(d(current_time))'''


'''from functools import reduce
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])
print("Fibonacci series upto 2:")
print(fib_series(2))
print("\nFibonacci series upto 5:")
print(fib_series(5))
print("\nFibonacci series upto 6:")
print(fib_series(6))
print("\nFibonacci series upto 9:")
print(fib_series(9))'''

s1 = 'A'
s2 = lambda func: func.lower()
print(s2(s1))


# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name.upper())
# lambda call
greet_user('Airborne Software')
# Output: Hey there, Delilah


