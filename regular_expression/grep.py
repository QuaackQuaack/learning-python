import re
inp = input('enter a input you want to find with caret ^ sign in front of i  ')
fhand = open('mbox.txt')
matched = 0 
for line in fhand:
    x = re.findall('\\b'+inp+'\\b',line)
    if len(x)>0:
        matched += 1 

print('the word',inp+ ' repeated',matched)

