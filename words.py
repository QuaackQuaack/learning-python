fhand = open('words.txt')
words = dict()
value = 1
 
for line in fhand:
    if line != '\n':
        fhand[line]=value
        value = value + 1

print(words)
