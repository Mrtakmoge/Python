class bank:
    def __init__(self):
        self.balance=int(input("Enter initialze amount:"))
        self.pin=1234
        
    def deposite(self):
        
        self.balance+=int(input("Enter amount to deposite:"))
        print("Amount deposited successfully...")
    def withdraw(self):
        self.amount=int(input("Enter amount to withdarw:"))
        if self.amount>self.balance:
            print("Insufficient balance...")
        else:
            self.balance-=self.amount
            print("withdraw successful...")
    
    def showbalance(self):
        print(f"current balance is {self.balance}")

a=bank()

while True:
        pin=int(input("Enter Pin:"))
        if pin==a.pin:
            break
        else:
            print("Incorrect Pin try agian...")
while True:
   
        
    print("1.showbalance")
    print("2.deposite")
    print("3.withdraw")
    print("4.exit")
    
    op=int(input("choose option:"))
    if op==1:
        print("="*10)
        a.showbalance()
        print("="*10)
    elif op==2:
        print("="*10)
        a.deposite()
        print("="*10)
    elif op==3:
        print("="*10)
        a.withdraw()
        print("="*10)
    elif op==4:
        exit()
    else:
        print("Invalid option...")
        
        