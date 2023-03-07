#while working on big project we need to be aware of moments in object like
# construction and destruction of object.This program is based on it.

class PartyAnimal:
    x = 0

    def __init__(self):
        print("I am constructed")

    def party(self):
        self.x = self.x + 1 
        print('So far,',self.x)

    def __del__(self):
        print("I am destructed",self.x)

an = PartyAnimal()
an.party()
an.party() # after this we can't call method because object is destroyed
an = 69 # after this line reuse variable 'an' to store it's new value i.e 69
print(an)# using constructor is quite frequent while destructor is not

