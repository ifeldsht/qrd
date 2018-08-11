from PIL import Image


w = 10
h = 10

# blue background
imglist = [(0,0,255) for x in range(w*h)]

# top, bottom
for i in range(w):
    imglist[i] = (255,0,0)
    imglist[(h-1)*w+i] = (255,0,0)

# left, right
for i in range(h):
    imglist[w*i] = (255,0,0)
    imglist[w*i+w-1] = (255,0,0)

# diagonals
for i in range(w):
    imglist[w*i+i] = (0,255,0)
    imglist[w*(i+1)-i-1] = (0,255,0)

img = Image.new("RGB",(w,h))
img.putdata(imglist)
img.save("11.png")

