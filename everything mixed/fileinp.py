file = input("enter the file name\t")
fhandle = open(file)
count = 0
for line in fhandle:
    if line.startswith('Subject:'):
        count = count + 1

print('there are',count,'subjects lines in ',file)


