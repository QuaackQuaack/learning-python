# this program is and example of initialization from class method and static method
class student:
    def __init__(self,first,last,attendance):
        self.first = first 
        self.last = last 
        self.email = first + '.' + last + '@company.com'
        self.attendance = attendance 

    @classmethod
    def from_std(cls, std_str):
        first , last , attendance = std_str.split('-')
        return cls(first,last,attendance)
    
    @staticmethod       # this is an example of static method which is independ of instance variable
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

std1 = 'wow-bow-983'
std2 = 'now-down-838'

new_std1 = student.from_std(std1)
print(new_std1.email)

import datetime
my_date = datetime.date(2016,7,11)

print(student.is_workday(my_date))

