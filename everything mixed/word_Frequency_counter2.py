import string
inp = input('enter a file name \t')

try:
    fhand = open(inp)

except:
    print('the file you want to open is not opening',inp)
    close()

counters = dict()

def counter():
    for line in fhand:
        line = line.translate(str.maketrans('','',string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            counters[word] = counters.get(word,0) + 1 

counter()
print(counters)
