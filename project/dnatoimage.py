from PIL import Image
import math  

with open("New Text Document.txt", "r") as f:
    seq = f.read().replace('\n','')


dimension = math.sqrt(len(seq))
x = round(4/3*dimension)
y = round(3/4*dimension)

img = Image.new("RGB", (x,y))

pixels = img.load()

num = 0

for i in range(x):
    for j in range(y):
        if seq[num] == "A" :
            temp = (0, 0, 1)
        elif seq[num] == "G" :
            temp = (0, 0, 2)
        elif seq[num] == "C" :
            temp = (0, 0, 3)
        elif seq[num] == "T" :
            temp = (0, 0, 4)
        pixels[i,j] = temp
        num+=1


img.show()