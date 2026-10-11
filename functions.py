
#Function defination:
def  calc_gst(price):#parameter 
    new_price=price+price*0.18
    print(new_price)

price=int(input("Enter Price:"))
#CAlling function
calc_gst(price)#argument

#built in function:
print("print is built in fuction in python")

#module functions:
from math import sqrt
print("square root of 16:",(sqrt(16)))

    