class Rectangle:

    def __init__(self, x, y, width, height, RGBcolor):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.RGBcolor = RGBcolor


    def draw(self, canvas):
        canvas.data[self.y:self.y +self.height, self.x:self.x +self.width] = self.RGBcolor
        

class Square:

    def __init__(self, x, y, side, RGBcolor):
        self.x = x
        self.y = y
        self.side = side
        self.RGBcolor = RGBcolor


    def draw(self, canvas):
        canvas.data[self.y:self.y + self.side, self.x:self.x +self.side] = self.RGBcolor