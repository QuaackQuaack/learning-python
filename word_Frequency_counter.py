import string
inp = input("enter a file you want to insert\t")

try:
    fhand = open(inp)

except:
    print("the file you entered can't be opened",fhand)
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

#to arrange the word 
arrange = list()
for key,value in list(counter.items()):
   arrange.append((value,key))

#to sort
arrange.sort(reverse = True)

#to print first ten maximum used words

need = int(input("how many words result do you want\t"))

for value,key in arrange[:need]:
    print(key,value)
