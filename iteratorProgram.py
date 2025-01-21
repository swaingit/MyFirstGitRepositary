import itertools
'''a=[1,2,3]
b=['a','b','c']
c=zip(a,b)
print(tuple(c))'''

'''for i in itertools.count(10,10):
    if i>=51:
        break
    else:
        print(i,end=" ")'''


'''temp=0
for i in itertools.cycle("*#@"):
    if temp>7:
        break
    else:
        print(i,end="-")
        temp=temp+1'''
a=1
while a<12:
    if a>4 and a<7:
        a=a+1
        continue
    
    else:
        print(a)
    a=a+1


