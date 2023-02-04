#program to differentiate between class vairable and istance vairable

class employee:
    raise_ok = 1.04
    num_of_emps = 0
    def __init__(self,first,last,pay):
        self.fname = first
        self.lname = last
        self.email = self.fname + '.' + self.lname + '@company.com'
        self.payment = pay

        employee.num_of_emps += 1

    def fullname(self):
        return f'{self.fname} {self.lname} has a salary of {self.payment}'

    def payment_raise(self):
        self.payment = int(self.payment * self.raise_ok)

emp1 = employee('corey','scafer',3984)
emp2 = employee('tes','testu',38495)

#print(emp1.__dict__)
emp1.raise_ok = 1.05
print(emp1.raise_ok)
print(employee.raise_ok)
print(employee.num_of_emps)


