#program to return payment of worker and give 1.5 time the hourly if they work  more than 40 hour

h = input("how many hour do you work?\t")
r = input("enter you rate of working?\t")

try:
    hour = float(h)
    rate = float(r)
    if hour > 40.0 :
        payment = hour*1.5*rate
    else:
        payment = hour * rate
    print(f"you payment is {payment} of total week ")

except:
    print("please enter numeric value")

