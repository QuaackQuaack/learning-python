file = input("enter the file name:   ")
fhand = open(file)
sum = 0.0
count = 0 
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        line1 = line.find(' ')
        line2 = line.find(' ')
        result = line[line1+1:line2+6]
        result = float(result)
        count = count + 1
        sum = result + sum 
 
final = sum/count

print("average spam confidence is \t",final)


