import re
x = 'Here is the bill of $10.00 sir'
y = re.findall('\$([0-9.]+)',x)
print(y)
 #if we need to extract special character like $ or caret(^) 
 #then we need to use \ 
