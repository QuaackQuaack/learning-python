# program to check whether the number is odd or even 
a  = input("Enter any number")
try:
    num = int(a)
    if num % 2 == 0 :
        print("entered number is even")
    else:
        print("Entered number is odd")
except:
    print("please enter interger number")

