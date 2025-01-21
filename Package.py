import module_one
import module_two
a=input("what do u want + for add,- for sub, s for ask ")
if a=="+":
    module_one.add()#by module_one(module/file name) we are calling function add() which is defined in module_one(module/file name)
if a=="-":
    module_two.sub()#by module_two(module/file name) we are calling function sub() which is defined in module_two(module/file name)
if a=="s":
    ask()


