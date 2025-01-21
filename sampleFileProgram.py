'''file_name=str(input("Enter the file name with .extension(exp-xyz.py,test.txt) :-"))#file name entered
file_object=open(file_name,'r')#file opened in read-r mode
read_line_by_line=file_object.readline()
while(read_line_by_line!=""):
    print(read_line_by_line)
    read_line_by_line=file_object.readline()#read the line by line until line is zero

file_object.closed()#file closed '''

f1=open("C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python313\\file_one",'r')
f2=open("copy.txt",'w')
for i in f1:
    f2.write(i)

print(f2)
    

              
