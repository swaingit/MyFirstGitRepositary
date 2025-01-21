'''#display not in both string
s1=input("Enter the first string")
s2=input("Enter the second string")
a=list(set(s1)^set(s2))
print ("The letters are ")
for i in a:
    print(i)'''

'''#display letter both first string but not in second string
s1=input("Enter the first string")
s2=input("Enter the second string")
a=list(set(s1)-set(s2))
print ("The letters are ")
for i in a:
    print(i)'''


#display letter in both string
s1=input("Enter the first string")
s2=input("Enter the second string")
a=list(set(s1)&set(s2))
print ("The letters are ")
for i in a:
    print(i)
