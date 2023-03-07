# to get oop from basic (example is from python for everyone)

class PartyAnimal():
    x = 0  # the data inside the object is called attributes

    def party(self): # functions inside the object is called methods 
        self.x = self.x + 1
        print("So,far",self.x)

an = PartyAnimal()  #defining 
print(an)
an.party() # object bitra ko function(method) call gareko 
an.party()
an.party()
PartyAnimal.party(an)
