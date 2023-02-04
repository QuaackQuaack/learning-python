class employee:
    no_of_emp  = 0 
    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first +'.' + last + '@company.com'
        self.pay = pay

        employee.no_of_emp +=1
    def fullname(self):
        return f'employee fullname is {self.first} {self.last}'
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    @classmethod #yo classmethod chai alternate classmethod ho 
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        cls(first,last,pay)

emp1_str = 'john-bon-38474'
emp2_Str = 'wow-bow-374484'

new_emp1 = employee.from_string(emp1_st)

print(employee.raise_amt)
employee.set_raise_amt(1.05)
print(employee.raise_amt)

print(new_emp1.email)
print(new_emp1.fullname())
