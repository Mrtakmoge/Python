#Q Write a function to check if a no. is even or odd:

def evenorodd(no):
    if no%2==0:
        print("no is even")
    else:
        print("No is odd")
        
no=int(input("Enter no:"))

evenorodd(no)

#Q WAF to count no. of vowels in a string

def v(string):
    count=0
    vowels="aeiou" 
    for i in string.lower():
        if i in vowels:
            count+=1
    print("No. of vowels:",count)           
  
v(input("Enter String:"))  

#Q WAF to print  if a no. is prime or not.

def p(num):
    factor_count=0
    for i in range(1,num+1):
        if num%i==0:
            factor_count+=1
            
    if factor_count==2:
        print(num,"is prime no.")
    else:
        print(num,"is not a prime no.") 
        
p(int(input("Enter num:"))) 

#Q WAF to return the average marks if a list of marks is passed as parameters:

List=[55,56,56,45]

    
    
def avg(Listofmarks):
    average=sum(Listofmarks)/len(Listofmarks)
    print("Avg marks of List:",average)
avg(List)
        
    
    
      