from students import Person

# this program is to learn inheritance from different files

class Hobbies(Person):  # here we had passed a class in another class 
                        #so while passing arguments we need to set it as 
    x = str()           #arguments of Person class (for eg line 13 and line 17)

    def activity(self,things): #here is self is written as conventional and things act as 
        self.things = things   # positional arguments
        print(f'{self.fname}{self.lname} hobbies is {self.things}.')

hobbies1 = Hobbies('pool','kun')
hobbies1.activity('dancing')


hobbies2 = Hobbies('passing','name')
hobbies2.activity('ludo')

