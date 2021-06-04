#pip3 install opencv-python
#pip3 install -U numpy
import cv2, numpy
imgr = cv2.imread("r.png")
imgg = cv2.imread("g.png")
imgb = cv2.imread("b.png")
imgc = cv2.imread("c.png")
imgm = cv2.imread("m.png")
imgy = cv2.imread("y.png")
r = 2
g = 1
b = 0
w = len(imgr[0])
h = len(imgr)
imgrgb = numpy.zeros([h, w, 3])
imgcmy = numpy.zeros([h, w, 3])
for x in range(0, w):
    for y in range(0, h):
        imgrgb[y][x][r] = imgr[y][x][r]
        imgrgb[y][x][g] = imgg[y][x][g]
        imgrgb[y][x][b] = imgb[y][x][b]
        
        imgcmy[y][x][r] = max(imgm[y][x][r], imgy[y][x][r])
        imgcmy[y][x][g] = max(imgy[y][x][g], imgc[y][x][g])
        imgcmy[y][x][b] = max(imgc[y][x][b], imgm[y][x][b])
        
cv2.imwrite("rgb.png", imgrgb)
cv2.imwrite("cmy.png", imgcmy)
print("Done!")
