#pip3 install opencv-python
#pip3 install -U numpy
import cv2, numpy
imggen = cv2.imread("gen.png")
r = 2
g = 1
b = 0
w = len(imggen[0])
h = len(imggen)
imgr = numpy.zeros([h, w, 3])
imgg = numpy.zeros([h, w, 3])
imgb = numpy.zeros([h, w, 3])
imgc = numpy.zeros([h, w, 3])
imgm = numpy.zeros([h, w, 3])
imgy = numpy.zeros([h, w, 3])
for x in range(0, w):
    for y in range(0, h):
        imgr[y][x][r] = imggen[y][x][r]
        imgg[y][x][g] = imggen[y][x][g]
        imgb[y][x][b] = imggen[y][x][b]

        imgc[y][x][g] = int((float(imggen[y][x][g]) + float(imggen[y][x][b])) / 2.0)
        imgc[y][x][b] = int((float(imggen[y][x][g]) + float(imggen[y][x][b])) / 2.0)

        imgm[y][x][r] = int((float(imggen[y][x][b]) + float(imggen[y][x][r])) / 2.0)
        imgm[y][x][b] = int((float(imggen[y][x][b]) + float(imggen[y][x][r])) / 2.0)
        
        imgy[y][x][r] = int((float(imggen[y][x][r]) + float(imggen[y][x][g])) / 2.0)
        imgy[y][x][g] = int((float(imggen[y][x][r]) + float(imggen[y][x][g])) / 2.0)
        
cv2.imwrite("r.png", imgr)
cv2.imwrite("g.png", imgg)
cv2.imwrite("b.png", imgb)
cv2.imwrite("c.png", imgc)
cv2.imwrite("m.png", imgm)
cv2.imwrite("y.png", imgy)
print("Done!")
