#in this code wwe will study about private access of class

class BankAccount:
    def __init__(self,accountholder):
        self._balance = 0 
        self._name = accountholder
        with open(self._name + 'ledger.txt','w') as ledgerfile:
            ledgerfile.write("balance is 0\n")

    def deposit(self,amount):
        if amount <= 0:
            return 'deposits'
        self._balance += amount 
        with open(self._name+'ledger.txt','w') as ledgerfile:
            ledgerfile.write('amount that is ' + str(amount) + '\n')
            ledgerfile.write('balance is' + str(self._balance)+ '\n')

    def withdraw(self,amount):
        if self._balance < amount or amount < 0 :
            return 'not enough in account or amount is to low to deposit'
        self._balance -= amount 
        with open(self._name+'ledger.txt','w') as ledgerfile:
            ledgerfile.write('amount that is withdraw ' + str(amount) + '\n')
            ledgerfile.write(f'balance is your accout is {self._balance} \n')
    
account1 = BankAccount('alice')
account1.deposit(999)
account1.withdraw(500)

account1._balance = 1000000000000 #well changing _balance outside the class is impolite
account1.withdraw(100)            #but we can. 

account1._name = 'bob' #without creating object i.e bob,we can explicitly edit name,bob.txt
account1.withdraw(1022)
