balance=float(input("enter balance:"))

def check_bal():
    global balance
    print("Balance:",balance)

def deposit():
    global balance
    amount=float(input("Enter amount to deposite:"))
    
    if amount<0:
        print(" amount can't be negative:")
    else:
        balance+=amount
        print("Deposite successful")

def withdraw():
    global balance
    
    amount=float(input("Enter amount to withdraw:"))
    
    if amount>balance or amount==0 :
        print("Insufficient balance")
    else:
        balance-=amount
        print("Withdraw successful")
print("="*5,"1.Balance","="*5)
print("="*5,"2.Deposite","="*5)
print("="*5,"3.Withdraw","="*5)
print("="*5,"4.Exit","="*5)
while True:
    

    op=int(input("Enter OPtion:"))
    if op==1:
        check_bal()
    elif op==2:
        deposit()
    elif op==3:
        withdraw()
    elif op==4:
        exit()
    else:
        print("Invalid option Try again")


        