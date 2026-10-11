class Account:
    
    def __init__(self,balance,accno):
        self.accno=accno
        self.balance=balance
    
    def debit(self):
        num=int(input("Enter the amount to debit:"))
        self.balance-=num
        print(num,"is debited from",self.accno)
        print("Current balance:",self.balance)
        
    def credit(self):
        num=int(input("Enter the amount to credit:"))
        self.balance+=num
        print(num,"is credited to acc",self.accno)
        print("Current balance:",self.balance)
        
    def bal(self):
        print("Current balace:",self.balance)
    
acc1=Account(100,995)

acc1.credit()
acc1.debit()
acc1.bal()
        
        
        
        
        
