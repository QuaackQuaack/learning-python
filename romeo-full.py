import string 
fhand = open('romeo-full.txt')
count = dict()
for line in fhand:
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word] +=1 


