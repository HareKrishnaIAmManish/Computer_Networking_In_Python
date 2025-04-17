class protocol:
    def __init__(self,name,number,description):
        self.name=name
        self.number=number
        self.description=description
    def getInfo(self):
        return self.name+"->"+str(self.number)+"->"+str(self.description)
myproto=protocol("mandy","-1","baigan")
print(myproto.getInfo())
print(myproto.description)

        
        