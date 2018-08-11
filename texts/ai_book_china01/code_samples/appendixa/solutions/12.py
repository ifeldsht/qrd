from PIL import Image

img = Image.open("12.jpg")

top = 10
bottom = 50
left = 5
right = 90

crop = img.crop( (left,top,right,bottom) )

crop.save("12_crop.jpg")


