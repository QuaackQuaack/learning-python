# this program is module of atm machine using OOP concept
#from frontatm import BasicInfo

class AtmMachine():
  def __init__(self,accountholder):
    self._accountholder = accountholder # _ before attribute is to denote that they are private 
    self._balance= 0
    with open(self._accountholder + 'ledger.txt','w') as ledgerfile:
      ledgerfile.write('your current balance is 0 \n')

  def deposit(self,amount):
    if amount < 0 :
      return #We can't deposit amount in negative 
    self._balance += amount
    with open(self._accountholder + 'ledger.txt','w') as ledgerfile:
      ledgerfile.write(f'Thank you for depositing {amount}\n')
      ledgerfile.write(f'you new balance is {self._balance}\n')

  def withdraw(self,amount):
    if self._balance < amount or amount < 0 :
      return #can't withdraw more amount than your actual bank balance
      self._balance -= amount
      with open(self._accountholder + 'ledger.txt','w') as ledgerfile:
        ledgerfile.write(f'you just withdrawal {amount}\n')
        ledgerfile.write(f'you current balance after withdraw is {self._balance}\n')

coustomer1 = AtmMachine('zoro')
print('which service do you want to use?')
print(''' 1) Deposit
      2) Withdraw
      3) Balance query ''')
entry = int(input())
if entry == 1:
    money = int(input('enter the amount you want to deposite \n'))
    coustomer1.deposit(money)
elif entry == 2:
    money = int(input("how much you want to withdrawal \n"))
    coustomer1.withdraw(money)
else:
    print('you amount is coustomer1._balance')
