fhand = open("romeo.txt",'r')
unique = []
file = fhand.read()
def removing():
    for line in file.split():
        if line not in unique:
            unique.append(line)

removing()
unique = sorted(unique)
print(unique)
