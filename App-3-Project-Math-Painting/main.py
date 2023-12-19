from canvas import Canvas
from shapes import Rectangle, Square


bkgrd = Canvas(1000,800,[255,255,255])

rect1 = Rectangle(x=10, y=10, width=100, height=200, RGBcolor=(0,0,255))
rect1.draw(bkgrd)

sq1 = Square(x=200, y=200, side=200, RGBcolor=[0,255,0])
sq1.draw(bkgrd)

bkgrd.save_img('first_attempt.jpg')