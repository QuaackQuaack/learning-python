# program to print out the day of week frim those line that start with from
fhand = open('python.txt')
count = 0 
for line in fhand:
    words = line.split()
    #print('debug:',words)
    if len(words) == 0 or words[0] != 'From' :continue
#    if  words[0] != 'From' : continue
    print(words[2])
