class Car:
    def __init__(self):
        self.race = False
        self.brk = False
        self.clutch = False
        
    def engine (self):
        self.race = True
        self.brk = True
        self.clutch = True
        print("car start")
s1 = Car()
s1.engine()        
        