import sys
from PIL import Image

img = Image.open(sys.argv[1])

imglist = list(img.getdata())

w, h = img.size

for i in range(h):
    row = ["0" if p>192 else "1" for p in imglist[(i*w):((i+1)*w)]]
    print "".join(row)

newimg = [(x,x,x) for x in imglist]
for i in range(100):
    newimg[i*w+i] = (255,0,0)
nimg = Image.new("RGB",img.size)
nimg.putdata(newimg)

nimg.save("test.jpg")
