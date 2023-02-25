sumk = 0
leg = 0 
avg = 0 
greatest = 0 
smallest = None 
while True:
    b  = input("enter a number:\t")
    if b  == "done":
            break
    else:
        a = int(b)         
        if greatest is None or a > greatest:
            greatest = a
        if smallest is None or a < smallest:
            smallest = a 
        sumk= int(sumk+a)
        leg = leg+1

print(sumk,leg)
print("greatest number is ",greatest)
print("smallest number is ",smallest)
