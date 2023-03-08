# in this code we will learn about private access in python 

class BankAccount:
    def __init__(self,accountHolder):
        self._balance = 0 # here balance method have single _ so it is private access
        self._name = accountHolder # only the code inside class can obtain data 
            with open(self._name + 'Ledger.txt','w') as ledgerfile:
                ledgerfile.write('\n balance is 0\n')
               
    def deposite(self,amount):
        if amount <= 0:
            return print("we don't allow negative ''deposite'' ")
        with open(self.name + 'Ledger.txt','w') as ledgerfile:
            ledgerfile.write('Deposit' + str(amount) +'\n')
            ledgerfile.write('balance is ' + str(self._balance) + '\n')

    

