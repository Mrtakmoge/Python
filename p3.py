#calculator
n1=float(input("Enter n1:"))
operator=input("Enter operator:")
n2=float(input("Enter n2:"))



if operator=="+":
    print(n1,"+",n2,"=",n1+n2)
elif operator=="-":
    print(n1,"-",n2,"=",n1-n2)
elif operator=="*":
    print(n1,"*",n2,"=",n1*n2)
elif operator=="%":
    print(n1,"%",n2,"=",n1%n2)
else:
    print("End of code")
    
    