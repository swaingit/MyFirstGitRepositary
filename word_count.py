'''file_name=str(input('Enter the file name'))
   word_count=0;
file_obj=open(file_name,'r')
for line in file_obj:
    word_list=line.split()#split() divided the line in file into words and store in list-word_list
    word_count=word_count+len(word_list)

print("Total number of words are", word_count)'''

'''#count the number of lines in files
file_name=str(input('Enter the file name'))
count_line=0
file_obj=open(file_name,'r')
for line in file_obj:
    
    count_line=count_line+1

print("Total number of words are",count_line)'''

'''#Read the text from keyboard and store in into the file and display it
file_name=str(input('Enter the file name'))
file_obj=open(file_name,'a')
text=input('Enter the text to store into the file')
file_obj.write(text)
file_obj.close()

file_obj2=open(file_name,'r')
line=file_obj2.readline()
while (line!=""):
    print(line)
    line=file_obj2.readline()

file_obj2.close()'''

'''#Find out the occurance of word in text
file_name=str(input('Enter the name of file with extesion'))
file_obj=open(file_name,'r')
to_search=input('Enter the word to search in the file')
occurance_word=0
for line in file_obj:
    word_list=line.split(" ")
    for i in word_list:
            if (to_search==i):
                occurance_word=occurance_word+1


print(occurance_word)'''


'''#find number of ocuurance of specific letter in text file
file_name=str(input("Enter the file_name :-"))
only_one_letter=input("Enter the only_one_letter:-")
count=0
file_obj=open(file_name,'r')
for line in file_obj:
    word_list=line.split()
    for word in word_list:
        for letter in word:
            if letter==only_one_letter:
                count=count+1
print(count)'''

'''#find number & print in text file
file_name=str(input("Enter the file_name :-"))
file_obj=open(file_name,'r')
for line in file_obj:
    word_list=line.split()
    for word in word_list:
        for letter in word:
            if letter.isdigit():
                print(letter)'''

'''#Print the content in reverse order               
file_name=str(input("Enter the file_name :-"))
for line in reversed(list(open(file_name))):
    print(line.rstrip())'''


