'''abc=[5,7,'a','b']
p=int(input("Enter the number"))
abc.append(p)
p=int(input("Enter the number"))
abc.append(p)
p=int(input("Enter the number"))
abc.append(p)
p=int(input("Enter the number"))
abc.append(p)
p=input("Enter the char")
abc.append(p)
p=input("Enter the char")
abc.append(p)
print(abc)
#del abc[3]
print(abc[3:5])
print(abc)'''
#zip list of tuple into list
list_=[(1,2),(2,3),(3,4)]
printlist((zip(*list_)))
