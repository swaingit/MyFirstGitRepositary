'''for loop
for a in range(10,1,-2):
    print(a)'''

'''
example of while loop
a=10
while a>1:
    print (a)
    a-=1
for t in range(5):
    print(t)'''
'''#Multiplication Table
number=int(input("Enter the number:-"))
for a in range(0,5):
    print(number," X ",a,'=',number*a)'''
    
    


'''#Factorial number of Input number
number=int(input("Enter the number  "))
sum=1
p=1
while number>0:
    sum=sum*number
    number-=1
    print("run of loop ",p,sum)
    p+=1
print(sum)'''

'''#Check Armstrong Number of any input number
number=int(input("Enter the number"))
check_=number
sum_=0;
Reminder=0;
while number>0:
    Reminder=number%10
    sum_=sum_+(Reminder)**3
    number=number//10

#print(sum_)
if sum_==check_:
    print("Input number is armstrong number")
else:
    print("input number is not armstrong number")'''

#Check Input number is perfect number or not
number=int(input("Enter the number to check perfect number:-"))
sum_=0
for a in range(1,number-1):
        if number%a==0:
            sum_=sum_+a
if number==sum_:
    print(number,'is perfect number')
else:
    print(number,'is not perfect number')


