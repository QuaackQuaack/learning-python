#here we will work with mulitple object 

class PartyAnimal:
    x = 0 
    name = str()

    def __init__(self,name): #initialize got printed while assiging the class like line 15
        self.name = name 
        print(self.name,'constructed')

    def party(self):
        self.x = self.x + 1 
        #we can deal with attribute of __init__ block
        print(self.name,'count of party has been',self.x)

name1 = PartyAnimal('cow')
name2 = PartyAnimal('buffalo')

name1.party()
name2.party()
name1.party()
