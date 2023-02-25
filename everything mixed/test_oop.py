class employee():
    def __init__(self,fname,lname,pay):
        self.first_name = fname 
        self.last_name = lname 
        self.email = fname + '.' + lname + '@company.com'
        self.salary = pay

    def fullname(self):
        return '{} {}'.format(self.first_name,self.last_name)

ep1 = employee('quantum','boy',9000)

print(ep1.fullname())

