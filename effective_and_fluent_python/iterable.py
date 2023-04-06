class Test:

    #constructor 
    def __init__(self,limit):
        self.limit = limit #body of construcotr

    def __iter__(self): #iterator initizalied
        self.x = 10
        #print(self) debug
        return self

    def __next__(self): #to move to next element 
        x = self.x # to store current value

        if x > self.limit: #which is 15 currently
            raise StopIteration

        self.x = x + 1
        return x 

for i in Test(15): #Prints number from 10 to 15
    print(i)

