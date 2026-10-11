class cmp:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def shownum(self):
        print(self.real,"i+",self.img,"j")
        
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return cmp(newReal,newImg)
        
        
        
        
c1=cmp(1,2)
c1.shownum()
c2=cmp(1,2)
c2.shownum()
c3=c1+c2
c3.shownum()