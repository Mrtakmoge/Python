#Conditional Statement:
#Syntax:
    # if condition:
    #     statement
    # elif condition:
    #     stmt
    # else condition:
    #     stmt
    
    
print("--------vote---------")
age=int(input("Enter age:"))
if age>=18:
    print("You are Eligible for vote")
else:
    print("You aren't Eligible for Vote")
    
print("-------comparison of 3 numbers----------")
    
n1=int(input("Enter number n1:"))
n2=int(input("Enter number n2:"))
n3=int(input("Enter number n3:"))
    
if n1>n2 and n1>n3:
        print("n1 is greater")
elif n2>n3 and n2>n1:
        print("n2 is greater")
else:
        print("n3 is greater")
        
print("----------Traffic Lights-------")

Light=input("Enter Light Color:")

if Light == "Green":
    print("GO")
elif Light == "Yellow":
    print("LOOK")
elif Light == "Red":
    print("Stop")
else:
    print("Light is broken")
    
    
    #ternery Operator:
    
T="vote" if age==18 else "can't vote"
print(T)

