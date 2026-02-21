class Circle:
    def __init__(self,radius):
        self.radius = radius
        
        
    def area(self):
        area = 3.14 * self.radius * self.radius
        print("Area of circle:",area)
    
    def perimeter(self):
        perimeter = 2 * 3.14 * self.radius 
        print ("Perimeter of circle:",perimeter)
        
s1 = Circle(5)
s1.area()
s1.perimeter()