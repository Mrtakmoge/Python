acc={
    "name":"Atharv Takmoge",
    "Age":20,
    "accnum":995,
    "pin":1234,
    "balance":1000
}


while True:
    if acc["pin"]==int(input("Enter PIN:")):
        print("Verfied successfully...")
        break
    else:
        print("Invalid PIN...")
while True:
        print("="*20)
        print("1.deposite")
        print("2.withdraw")
        print("3.View Balance")
        print("4.exit")
    
        op=int(input("Enter option:"))
        if op==1:
            amount=int(input("Enter amount to deposite:"))
            if amount ==0:
                print("amount cant be zero or negative")
            else:
                acc["balance"]+=amount
                print("Deposite successful...")
        elif op==2:
            amount =int(input("Enter amount to withdraw:"))
            if amount>acc["balance"]:
                print("Insufficient balance")
            else:
                acc["balance"]-=amount
                print("Withdrawl successful...")
        elif op==3:
            print("balance=",acc["balance"])
        elif op==4:
            exit()
        else:
            print("Invalid option ...")            