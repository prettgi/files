from canvas import Canvas
from shapes import Rectangle, Square


bkgrd = Canvas(1000,800,[255,255,255])

rect1 = Rectangle(x=100, y=100, width=100, height=200, RGBcolor=(0,0,255))
rect1.draw(bkgrd)

sq1 = Square(x=200, y=200, side=200, RGBcolor=[0,255,0])
sq1.draw(bkgrd)

rect2 = Rectangle(x=210, y=340, width=200, height=300, RGBcolor=(255,0,255))
rect2.draw(bkgrd)

sq2 = Square(x=350, y=250, side=300, RGBcolor=[0,255,255])
sq2.draw(bkgrd)

bkgrd.save_img('first_attempt.jpg')