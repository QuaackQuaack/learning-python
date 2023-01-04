sum = 0
count = 0 
print("Print done if you had entered every input")
try:
    while True:
        num = input("Enter the number you want to \t")
        if num == "done": break
        count +=1
        num = float(num)
        sum = sum + num
except :
    print("please enter valid input\n")
avg = sum / count
print("the average of entered number is \t ",avg)
 

