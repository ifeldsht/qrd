import PIL 
from PIL import Image

img = Image.open("12.jpg")

img.transpose( PIL.Image.FLIP_TOP_BOTTOM ).save("13_flip1.jpg")
img.transpose( PIL.Image.FLIP_LEFT_RIGHT ).save("13_flip2.jpg")

