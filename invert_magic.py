class Car:

    def __invert__(self):
        return "hello"
    

car = Car()
print(~car) # This stands for bitwise not


class AreaOrPerim:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return ""+str(self.width * self.height) # If directly called will return area
    
    def __invert__(self):
        return 2*(self.width + self.height) # if inversely called will return perimeter
    

area = AreaOrPerim(width=20, height=20)
print(area)
print(~area)