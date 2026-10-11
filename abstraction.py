class car:#Abstraction:hiding the implementation details of class and showing the essential feature to user 
    def __init__(self):
        self.brk=False
        self.acc=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("Car started")
car1=car()
car1.start()