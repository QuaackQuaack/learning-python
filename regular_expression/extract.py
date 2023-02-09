import re
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)',line)
    if len(x) > 0:
        print(x)

#yo program ley chai search ra findall 
# both ko kam garxa hana 
# .findall ma () rakhe paxi hamley floating number 
# extract garna milxa 
