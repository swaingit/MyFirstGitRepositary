def AppendTextInFile():
        file_name=str(input("Enter the file name"))
        text=input("Enter the text to add in file 'file_name':-")
        file_obj_1=open(file_name,'a')
        file_obj_1.write(text)
        file_obj_1.close()
        print("Let's see content in file file_name after appending the text ")
        file_obj2=open(file_name,'r')
        line=file_obj2.readline()
        while (line!=""):
            print(line)
            line=file_obj2.readline()#increment to next line

        file_obj2.close()

def CreateNewFile():
        file_name=str(input("Enter the new file name:-"))
        file_obj=open(file_name,'w')
        file_obj.close()

def CountSpecificLetterInFile():
        file_name=str(input("Enter the file name "))
        letter=input("Enter the letter to count number of occurance in file")
        count=0
        file_obj_1=open(file_name,'r')
        line=file_obj_1.readline()
        for l in line:
            word_list=l.split()
            for word in word_list:
                    for char in word:
                        if char==word:
                            count+=1
        print("The number occurance of entered letter",letter,"is-",count)


def CountWordInFile():
        file_name=str(input("Enter the file name file_name "))
        countWord=0
        file_obj=open(file_name,'r')
        line=file_obj.readline()
        for i in line:
            word_list=i.split()
            length=len(word_list)
            countWord=countWord+length

        print("Total number of word in file",file_name,"is :-", countWord)

             
number=input("Enter the number in letter like- one two three, four, five ")
if number=='one':
    AppendTextInFile()
elif number=='two':
    CreateNewFile()
elif number=='three':
    CountSpecificLetterInFile()
elif number=='four':
    CountWordInFile()
else:
    exit()
        
        
