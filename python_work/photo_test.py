import numpy as np
from PIL import Image
img = Image.open(r"C:\Users\Bxf\Pictures\Genki Arcade - 2021-10-31 051004.jpg")
a = np.array(img)
print("a.shape={}, a.dtype={}, a[0,0,:]={}".format(a.shape, a.dtype, a[0,0,:]))

b = 255 - a 
im = Image.fromarray(b.astype('uint8'))
im.show()

c = a.copy()
c[::2] = 0
l = Image.fromarray(c)
l.show()

d = a.copy()
d[:,::2] = 255
k = Image.fromarray(d)
k.show()
