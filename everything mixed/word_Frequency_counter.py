import string
inp = input("enter a file name you want to open")

try:
    fhand = open(inp)
except:
    print("the file you want to open is not working ",inp)
    close()

counter = dict()

def word_counter():
    for line in fhand:
        line = line.translate(str.maketrans('','',string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            counter[word] = counter.get(word,0) + 1 
word_counter()

arrange = list()
for key,value in list(counter.items()):
    arrange.append((value,key))


arrange.sort(reverse = True)

print(arrange)
