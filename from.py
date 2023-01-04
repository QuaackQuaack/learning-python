fhand = open('mbox.txt')
email = list()
count = 0 
for line in fhand:
    if line.startswith('From '):
        line = line.strip()
        line = line.split()
        print(line[1])
        count += 1

print("there were",count,"line in the file with From as the first word")
