'''class rectangle():
    def __init__(self,breadth,length,name):
        self.breadth=breadth
        self.length=length
        self.name=name
    def area(self):
        return self.breadth*self.length
    def print_(self):
        print(self.name)

a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))

obj=rectangle(a,b,'chandra')
print("Area of rectangle:",obj.area(),obj.print_())
#print()'''

class sub:  
    def f1(self, s1):  
        return self.f2([], sorted(s1))  
 
    def f2(self, curr, s1):  
        if s1:  
            return self.f2(curr, s1[1:]) + self.f2(curr + [s1[0]], s1[1:])  
        return [curr]  
a=[]
n=int(input("Enter number of elements of list: "))
for i in range(0,n):
    b=int(input("Enter element: "))
    a.append(b)
print("Subsets: ")
print(sub().f1(a))
