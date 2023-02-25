fhand = open('romeo.txt','r')
file = fhand.read()
result = dict()
words = file.split()

for line in words:
    result[line] = result.get(line,0) + 1 

print(result)
    
