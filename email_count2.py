inp = input("enter a file name you want to open ")
try:
    fhand = open(inp)

except:
    print("entered file can't be opened ",inp)
    close()
email = list()
def separating():
    for line in fhand:
        line = line.split()
        if len(line)==0 or line[0]!='From' : continue
        else:
            email.append(line[1])

separating()
repeat = dict()
def repeatation():
    for line in email:
        repeat[line] = repeat.get(line,0) + 1  
repeatation()
print(repeat)

#to print maximum email send by the user
value = repeat.values()
maximum = max(value)
for line in repeat:
    if maximum == repeat.get(line,0):
        print("the email with maximum msg is " , line , maximum)


