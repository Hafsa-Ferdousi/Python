class Shape():
    def  area(self):
        return "Undefined"

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l=l
        self.w=w

    def  area(self):
        return   self.l * self.w


class Circle(Shape):
    def __init__(self, r):
        self.r= r


    def area(self):
        return 3.14* self.r **2

shape= [Rectangle(2,5), Circle(5)]
for shapes in shape:
    print(f"Area:{shapes.area()}")

