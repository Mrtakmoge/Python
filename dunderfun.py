class order:
    def __init__(self):
        self.item=input("Enter item:")
        self.price=float(input("Enter Price:"))
        
    def __gt__(self,odr2):
        if self.price>odr2.price:
            print("Order 1 greater than order 2")
        else:
            print("Order 2 is greater than order 1")
            
o1=order()

o2=order()

o3=o1>o2

        