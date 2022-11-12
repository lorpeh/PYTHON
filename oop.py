class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return (self.length + self.width)

    def Area(self):
        return (self.length* self.width)
    
    def display(self):
        return(self.length, self.width)

# rectangle = Rectangle(10, 20)
# print(rectangle.Perimeter())
# print(rectangle.Area())
# print(rectangle.display(), rectangle.Perimeter(), rectangle.Area())

class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self,length, width)
        self.height = height
        
    
    def Volume(self):
        return(self.length * self.width * self.height)

para = Parallelepipede(10, 20, 30)
print(para.Volume())




        
    
