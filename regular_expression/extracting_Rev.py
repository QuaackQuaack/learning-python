import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9]+)',line)
    if len(x) > 0:
        print(x)

#to find the line starting from Details we used ^details
# to find the other character followed by it is .*
# to find rev  and one or more digits ko lai + 
# for extracting chai paranthesis use garim ()
