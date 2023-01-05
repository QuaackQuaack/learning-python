import string
fhand = open('romeo-full.txt')
count = dict()
for line in fhand:
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        count[word] = count.get(word,0) + 1 



#sorting the dict my value wise

lst = list()
for key,val in list(count.items()):
    lst.append((val,key))


lst.sort(reverse = True)

for value,key in lst[:10]:
    print(key,value)
