inp = input("enter a file name you want to open: ")
try:
    fhand = open(inp)
except:
    print("Entered file can't be open ",fhand)
    close()
wow = list()
result = dict()
def separating_weeks():
    for line in fhand:
        line = line.rstrip()
        words = line.split()
        if len(words) == 0 or words[0] != "From": continue
        else:
            wow.append(words[2])

separating_weeks()
for line in wow:
    result[line] = result.get(line,0) + 1 

print(result)


        
    

