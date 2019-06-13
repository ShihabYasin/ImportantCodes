import os
from PIL import Image
import PIL.ImageOps
import numpy

files = [f for f in os.listdir('in')]
for f in files:
    image = Image.open("in/"+f)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save("out/"+f)