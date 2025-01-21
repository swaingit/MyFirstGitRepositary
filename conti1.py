def ask():
    a=input("enter name ")
    b=input("enter company name  ")
    c=int(input("enter mob no   "))
ask()
while 1:
    ch=input("do u want to continue y/n ")
    if ch=="y" or ch=="Y":
        ask()
    else:
        break
