class Cars:
    def __init__(self, make = None, model = None, year = None, color = None,price = None):
        self.make = make
        self.model = model
        self.year = year 
        self.color = color 
        self.price = price
        
    def setcolor(self, color):
        self.color = color
    def getcolor(self):
        return self.color
    def setmake(self, make):
        self.make = make
    def getmake(self):
        return self.make
    def setmodel(self, model):
        self.model = model
    def getmodel(self):
        return self.model
    def setyear(self, year):
        self.year = year
    def getyear(self):
        return self.year
    def setprice(self, price):
        self.price = price
    def getprice(self):
        return self.price