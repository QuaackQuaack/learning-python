#WAP that ask user for a list of number and prints out the max and min from the entered number 

number = list()
print("enter done when you end ")
while True:
    inp = (input("enter a number:\t"))
    if inp == "done" : break
    inp = int(inp)
    number.append(inp)

print("Maximum: ",max(number))
print(" Minimum: ",min(number))


