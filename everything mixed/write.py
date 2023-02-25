file = input("enter the name of the file you want \t")
fhand = open(file,'w')
line1 ="this should be the first line of the box."
fhand.write(line1)
line2="this is 2nd line of the box"
fhand.write(line2)
fhand.close()

