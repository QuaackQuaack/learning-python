inp= input('enter a file name: ')
try:
    fhand = open(inp)

except:
    print("your entered file can't be opened", inp)
    close()

email = list()
result = dict()
def separating_email():
    for line in fhand:
        line = line.split()
        if len(line) == 0 or line[0] != 'From': continue
        else:
            email.append(line[1])
separating_email()
def email_histogram():
    for line in (email):
        result[line] = result.get(line,0) + 1
email_histogram()    
print(result)
repeatation = result.values()
maximum = max(repeatation)
for line in result:
    if maximum == result.get(line,0):
        print('email is ',line,'and',maximum)









