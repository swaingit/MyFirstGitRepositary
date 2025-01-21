'''#Find the number of Vowels in string using state
s=input("Enter the string:-")
count=0;
vowels = set("aeiou")
for i in s:
    if i in vowels:
        count+=1

print("Total number of Vowels in string",count)'''

s1=input("Enter the first string")
s2=input("Enter the second string")
#a=list[set(s1),set(s2)]
a=list(set(s1)&set(s2))
for i in a:
    print(i)


