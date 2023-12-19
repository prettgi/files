import numpy as np 
from PIL import Image

class Canvas:

    def __init__(self, width, height, RGBcolor):
        self.width = width
        self.height = height
        self.RGBcolor = RGBcolor

        self.data = np.zeros((self.width,self.height,3),dtype=np.uint8)
        self.data[:] = self.RGBcolor 

    def save_img(self, img_path):
        img = Image.fromarray(self.data, 'RGB')
        img.save(img_path)