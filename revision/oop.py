class employee:
    
    def __init__(self,first,last,pay):
        self.fname = first
        self.lname = last
        self.email = first + '.' + last + '@company.com'
        self.payment = pay

    def fullname(self):
        return  f'{self.fname} {self.lname} is good boy with payment {self.payment}'

emp1 = employee('corey','schafer',5000)
emp2 = employee('test','name',3939)

print(emp1.fullname())




