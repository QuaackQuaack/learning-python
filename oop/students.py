#this program is to revison everything like 
# like multiple instances and inheritance 
# may be also cycle of class 

class Person:
     x = 0 
     def __init__(self,fname,lname):
         self.fname = fname
         self.lname = lname 
         self.email = fname + "." + lname + "@gmail.com"
         print(self.email,"has been constructed")

     def full_name(self):
        return f'Student full name is {self.fname} {self.lname}'

     def runner(self):
         self.x = self.x + 1
         print(" this loop is running ",self.x,'times')

name1 = Person('corey','schafer')
name2 = Person('zoro','kun')
print(name1.full_name())
print(name2.full_name())
name1.runner()
name2.runner()
