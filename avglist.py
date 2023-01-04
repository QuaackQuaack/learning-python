numlist = list()
while True:
    inp = input("enter the value you want to enter")
    if inp =="done" : break
    value = float(inp)
    numlist.append(value)
    print(numlist)

avg = sum(numlist)/len(numlist)
print("average is \t ",avg)
