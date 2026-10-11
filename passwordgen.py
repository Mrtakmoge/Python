import random
import string

password=""
op=string.ascii_letters+string.digits+string.punctuation
n=int(input("Enter len of password::"))

for i in range(n):
    password+=random.choice(op)
    
print(password)