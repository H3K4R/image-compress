import PIL
from PIL import Image

mywidth=1908
myheight=1146

img=Image.open('ron.jpg')
img=img.resize((mywidth, myheight),PIL.Image.ANTIALIAS)
img.save('resize.jpg')