#Calculator:

while True:
    print("="*10)
    n1=float(input("Enter n1:"))
    op=input("Enter operatoration to perform:")
    n2=float(input("Enter n2:"))
    print("="*10)
    
    
    
    if op=="+":
        print(n1+n2)
    elif op=="-":
        print(n1-n2)
    elif op=="*":
        print(n1*n2)
    elif op=="/":
        print(n1/n2)
    elif op=="exit":
        exit()
    else:
        print("Invalid operator")