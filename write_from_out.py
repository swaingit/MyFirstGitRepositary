'''with open("chand","w") as f:
    while 1:
        t=input("jhgfhg  ")
        f.write(t)
        if t=="@":
            break'''



fname=input('Enter the file name')
file3=open(fname,"a")
text=input("Enter the string to append:\n")
file3.write("\n")
file3.close()
print("Content of appended file:")
file4=open(fname,'r')
line1=file4.readline()
while(line1!=""):
    print(line1)
    line1=file4.readline()

file4.close()
