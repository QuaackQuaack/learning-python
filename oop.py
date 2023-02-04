class employee():
    def __init__(self,fname,lname,pay):
        self.first_name = fname
        self.last_name = lname 
        self.email = self.first_name + '.' + self.last_name + '@company.com'
        self.payment = pay

    def fullname(self):
        return '{} {}'.format(self.first_name,self.last_name)

emp1 = employee('Ronoro','Zoro',8000)
print(emp1.fullname())
print(employee.fullname(emp1))
print('the salary is {} ' .format(emp1.payment))

