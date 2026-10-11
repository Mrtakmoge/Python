import string
import random


characters=string.ascii_letters+string.punctuation+string.digits

password=""
pass_len=int(input("Enter lenght of password: "))
for i in range(pass_len):
    password+=random.choice(characters)
print(password)
    

