class student:
    name="Atharv"#class attr
    
    def __init__(self,fullname,marks):#default constuctor
        self.name=fullname#obj attr
        self.marks=marks
        print("Creating new student ")
        #methods:   
    def hello(self):
        print("hello",self.name)
        
    def get_marks(self):
        print(self.marks)
    
    
s1=student("Rohit",89)#printing obj attr
print(s1.name,s1.marks)
#obj attr has higher precedence than class attr
print(student.name)#printing class attr



s2=student("Diksha",99)
print(s2.name,s2.marks)

s3=student("atharv",87)
s3.hello()
s3.get_marks()
    
