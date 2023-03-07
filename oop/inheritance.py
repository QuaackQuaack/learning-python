from multipleinstances import PartyAnimal #this one is explicit importing
#next one importing is through namespace 

class CricketFan(PartyAnimal): # for understanding it's like pasing class inside class
   points = 0
   def six(self):
      self.points = self.points + 6
      self.party()
      print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()

