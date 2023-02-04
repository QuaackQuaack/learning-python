class student:
    no_of_std = 0 
    increase_attendance = 1.04 


    def __init__(self,fname,lname,attendance,grade):
        self.fname = fname
        self.lname = lname
        self.attendance = attendance
        self.grade = grade

        student.no_of_std += 1 

    def fullname(self):
        return f'your full name is {self.fname} {self.lname}'

    def increase_attend(self):
        self.attendance = int(self.attendance * student.increase_attendance)
    @classmethod
    def set_raise_amt(cls,amount):
        pass



std_1 = student('arjun','kharal',29,12)
std_2 = student('corey','schafer',22,18)
std_3 = student('pravesh','bhay',32,5)

print(std_1.fname)
#print(f'student no 2 , full name is {std_2.fname} {std_2.lname}')

print(std_1.fullname())
print(student.no_of_std)

print(student.increase_attendance)



