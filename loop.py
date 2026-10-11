nums=range(1,6)#range(start value,stop value,step value)
print("Range():")
print(nums)

i=5
#while loops:
print("While loops:")
while i>=1:
    print(i*"*")
    i-=1
    
#for loop:
print("For loops:")
nums=range(1,6)
for i in range(1,6):
    print(i)
    
#Q print 1 to 10 even no.s
print("Print even no.s:")
for i in range(1,11):
    if i%2==0:
        print(i)
        
for i in range(2,11,2):
    print(i)
    
#Print multiple of 3:
print("Multiple of 3 from 1 to 21")
for i in range(1,50):
    if i==21:
        break
    if i%3==0:
        print(i)
        
