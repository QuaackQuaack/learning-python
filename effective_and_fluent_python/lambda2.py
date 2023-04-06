
even_list = [ arg * 10 for arg in range(1,5)]

for item in even_list:
    print(item)


#by lambda method 

even_list = [ lambda arg = x : arg * 10 for x in range(1,5)] #lamda makes evenlist object that holds function's object 
#print(even_list) #here we can't call even_list cause list object is not callable
for item in even_list:
    print(item())
