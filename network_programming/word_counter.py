import urllib.request, urllib.parse, urllib.error
urlhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = dict()
for line in urlhand:
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word,0) + 1 

arrange = list()
for key,value in list(count.items()):
    arrange.append((value,key))

arrange.sort(reverse = True)
print(arrange)
