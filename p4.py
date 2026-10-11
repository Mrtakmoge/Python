#Q Print all odd no.s from 1 to 20
print( "Q1 Odd no.s from 1 to 20:")
for i in range(1 ,20,2):
    print(i)
    
#Q2print table of 57:
print("Q2 Print table of 57:")

for i in range(1,11):
    print(57*i)
    
print("Q3 print all multiples of 3 from 1 to 50 but skip 15")

for i in range(1,51):
    if i==15:
        
        continue
    if i%3==0:
        print(i)

print("Q4 Take two integers as a and b as input. Find and print the first no. between 1 and 1000 that is divisible by both no.s")   

a=int(input("Enter no. a :"))
b=int(input("Enter no. b:"))

for i in range(1,1001):
    if i%a==0 and i%b==0:
        print(i)
    