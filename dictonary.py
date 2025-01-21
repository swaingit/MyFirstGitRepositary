'''d1={'A':1,'B':2}
d2={'C':3}
d1.update(d2)
print("the concatinated dictionary is :-")
print(d1)'''

'''n=int(input("Enter the number"))
d={n:n*n for i in range(1,n+5)}
print(d)'''

'''d={'a':1,'b':2,'c':3}
print(d)
key=input("Enter the key to delete from dictonary:-")
if key in d:
    del d[key]
else:
    print("key not found")
    exit(0)
print(d)'''

'''key=[]
value=[]
print('Enter the 4 keys for key list:-')
for i in range(0,4):
    key_ele=input("Enter the key_ele for key list:-")
    key.append(key_ele)
print('Enter the 4 values for value list')
for i in range(0,4):
        value_ele=int(input("Enter the value_ele for value list:-"))
        value.append(value_ele)

d=dict(zip(key,value))

print(d)'''


    
