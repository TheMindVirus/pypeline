#pip3 install opencv-python
#pip3 install -U numpy
import cv2, numpy, math
imgcrs = cv2.imread("crs.png")
r = 2
g = 1
b = 0
w = len(imgcrs[0])
h = len(imgcrs)
px = 0.0
py = 0.0
pr = 0.0
pg = 0.0
pb = 0.0
a = 255.0
imgint = numpy.zeros([h, w, 3])
for x in range(0, w):
    px = x / w
    pr = (2.0 - abs(6.0 * px)) if (px < 0.5) else (2.0 - abs(6.0 * (px - 1.0)))
    pg = 2.0 - abs(6.0 * (px - (1.0 / 3.0)))
    pb = 2.0 - abs(6.0 * (px - (2.0 / 3.0)))
    pr = 255.0 if (pr > 255.0) else 0.0 if (pr < 0.0) else pr
    pg = 255.0 if (pg > 255.0) else 0.0 if (pg < 0.0) else pg
    pb = 255.0 if (pb > 255.0) else 0.0 if (pb < 0.0) else pb
    avgr = 0.0
    avgg = 0.0
    avgb = 0.0
    for y in range(0, h):
        py = 1.0 - (y / h)
        avgr += float(imgcrs[y][x][r])
        avgg += float(imgcrs[y][x][g])
        avgb += float(imgcrs[y][x][b])
    avgr /= h
    avgg /= h
    avgb /= h
    for y in range(0, h):
        py = 1.0 - (y / h)
        imgint[y][x][r] = avgr
        imgint[y][x][g] = avgg
        imgint[y][x][b] = avgb
cv2.imwrite("int.png", imgint)
print("Done!")
