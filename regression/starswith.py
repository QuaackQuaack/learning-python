import re
fhand = open("mbox.txt")
for line in fhand:
    line = line.strip()
    if re.search('^From:.+@',line):
        print(line)
