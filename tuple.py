'''
# Python program to create Tuples
print("Python program to create Tuples")
num = (100, 200, 300, 400)
print(num)

#add a number in tuple
print("add a number(900) in tuple")
num=num+(900,)
print(num)

#add at specific index
print("add a numbers(301,302) in specific index :2")
num=num[:2]+(301,302)
print(num)

#convert tuple into list
print("convert tuple into list")
to_list=list(num)
print(to_list)

#add number in list at end
print("add number 0 in list at end")
to_list.append(000)
print(to_list)

#convert tuple into list
print("convert the list into tuple")
to_tuple=tuple(to_list)
print(to_tuple)

#add a number in tuple
print("add a number in tuple")
to_tuple=to_tuple+(120,121,)
print(to_tuple)

#Convert tuple to string
tup=('a','b','c')
str=''.join(tup)
print("After joining the tuple with string is")
print(str)'''

'''#check element in tuple and number of ocuurance of element and find the element in nth position in tupe
tup=('A',1,'B',2,'C',3,'D',5.7,3,5,2)
print(5.6 in tup)
print('A' in tup)
count=tup.count(3)
print(count)
item=tup[4]#C
print(item)
item_2=tup[6]
print(item_2)'''

#Remove element from tuple
tuple_of_pairs=(('a',6),'b', 'c')
p=reversed(tuple_of_pairs)
print(tuple(p))
