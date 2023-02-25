#1.5 time the more of the pay if he/she does overtime work
a = float(input("enter you working hour"))
b = float(input("enter your rate of working"))
def payment(hour,rate):
    if hour > 45.0:
        payment = hour * rate * 1.5 
    else:
        payment = hour * rate
    return payment

pay = payment(a,b)
print(pay)


