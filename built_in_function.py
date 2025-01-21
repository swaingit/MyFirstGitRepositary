'''x=ord('a')
print(x)'''
'''x=pow(3,2)
print(x)'''
'''list_=[1,2,3]
print(list_)
a=reversed(list_)
for i in a:
    print(i)'''

'''x=round(7.7455,2)
print(x)'''

'''x=set(('apple','banana','greep'))
print(x)'''

'''a=(1,2,3,4,5)
x=slice(2)
print(a[x])#Ans-(1, 2)'''

'''a=(2,0,44,8,9,98)
print(sorted(a))#Ans-[0, 2, 8, 9, 44, 98]'''

'''x=str(23.09)
print(x)
print(type(x),x)#Ans-<class 'str'> 23.09'''

'''a=(2,0,44,8,9,98)
x=sum(a)
print(x)#Ans-161'''

'''text="this is chandra"
print(text.capitalize())#Ans-This is chandra'''

'''text="HARI IS A SOFTWARE ENGINEER"
print(text.casefold())#Ans-hari is a software engineer'''

'''text_a=('a','b','c')
text_b=('A','B','C')
zip_=zip(text_a,text_b)
print(list(zip_))#Ans-[('a', 'A'), ('b', 'B'), ('c', 'C')]'''

'''text="chandra jhnjkmkm chandra hbvjhjnjmkkj   chandra vbhnjnmk"
print(text.count('chandra'))# Ans-3'''

'''text="hello how are you."
x=text.endswith(".")
print(x)#Ans-true'''


'''text="hello how are you."
x=text.encode()
print(x)#Ans-b'hello how are you.'''

'''text="c\th\ta\tn\td\tr\ta"
x=text.expandtabs()
print(x)#Ans-c       h       a       n       d       r       a'''

text="hello how 123 @ are you."
digit="1237"
space_=" "
a=text.find("how")
a_=text.index("how")
result=text.isalpha()
print(result)#false
print(a)#6
print(a_)#6
print(digit.isdigit())#true
print(text.islower())#true
print(digit.isnumeric())#true
print(space_.isspace())#true
title_="Hello How Are You."
print(title_.istitle())#true(all first char is capital)
upper="UPPER LETTER"
print(upper.isupper())#true
x=title_.ljust(56)
#print(x,"i am good")#Hello How Are You.                                       i am good
x_=title_.rjust(56)
print(x_," good good good")#                                      Hello How Are You.  good good good
print(upper.lower())#upper letter
s="i can eat apple a day,apple is liking fruit"
x=s.rpartition("apple")
print(x)#('i can eat apple a day,', 'apple', ' is liking fruit')
print(s.splitlines())#['i can eat apple a day,apple is liking fruit']
print(s.replace("apple", "mango"))#i can eat mango a day,mango is liking fruit
print(s.title())#I Can Eat Apple A Day,Apple Is Liking Fruit
print(s.upper())#I CAN EAT APPLE A DAY,APPLE IS LIKING FRUIT







