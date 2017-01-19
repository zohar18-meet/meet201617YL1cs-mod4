import turtle
from rectangle import Rectangle
class Square(Rectangle) :
    def __init__(self,height):
        super(Square,self).__init__(height,height)
    def set_height(self, height):
        super(Square,self).set.length(height)
        new_height=self.height
        new_length=self.height
    
    def get_area(self):
        """
        Calculate the area of the shape
        """
        return self.length*self.height

    def draw_shape(self):
        """
        Draw the shape, starting at 0,0.

        If any old drawings exist, remove them.
        """
        self.turtle.clear() #Remove old drawings (if they exist)
        self.turtle.penup()
        self.turtle.goto(0,0)
        self.turtle.pendown()
        self.turtle.goto(self.length,0)
        self.turtle.goto(self.length,self.height)
        self.turtle.goto(0,self.height)
        self.turtle.goto(0,0)
        self.turtle.penup()
        self.has_been_drawn=True
