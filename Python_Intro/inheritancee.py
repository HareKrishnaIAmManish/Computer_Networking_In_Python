# class myList(list):
#    def max_min(self):
#       return max(self),min(self)
# myList= myList()
# myList.extend((100,200,300,500))
# print(myList)
# print(type(myList.max_min()))
# print(myList.max_min())
class class1:
    def __init__(self,number):
       self.number=number 
class class2():
    def __init__(self,description):
        self.descr=description
class class3(class1,class2):
    def __init__(self,number,desc):
        class1.__init__(self,number)
        class2.__init__(self,desc)
myobj=class3(-1,"baigan")
print(f"{myobj.descr} and {myobj.number}")





