fhand = open("romeo.txt")
unique = list()
result = list()


for line in fhand:
    line = line.strip()
    line = line.split()
    for t in range(0,len(line)):
        result.append(line[t])

 
for x in range(0,len(result)):
    word = result[x]
    if (word in unique) ==  False:
        unique.append(word)
       

unique.sort()
print(unique) 
