#pip3 install opencv-python
#pip3 install -U numpy
import cv2, numpy, math
r = 2
g = 1
b = 0
w = 1920
h = 1080
px = 0.0
py = 0.0
pr = 0.0
pg = 0.0
pb = 0.0
a = 255.0
imggen = numpy.zeros([h, w, 3])
for x in range(0, w):
    px = x / w
    pr = (2.0 - abs(6.0 * px)) if (px < 0.5) else (2.0 - abs(6.0 * (px - 1.0)))
    pg = 2.0 - abs(6.0 * (px - (1.0 / 3.0)))
    pb = 2.0 - abs(6.0 * (px - (2.0 / 3.0)))
    print(min(max(int(pr * 255.0), 0), 255),
          min(max(int(pg * 255.0), 0), 255),
          min(max(int(pb * 255.0), 0), 255))
    for y in range(0, h):
        py = 1.0 - (y / h)
        dy = 1.0 - py
        dr = 1.0 - pr
        dg = 1.0 - pg
        db = 1.0 - pb
        imggen[y][x][r] = a * (((2.0 * py) * pr) if (py < 0.5) else (1.0 - ((2.0 * dy) * dr)))
        imggen[y][x][g] = a * (((2.0 * py) * pg) if (py < 0.5) else (1.0 - ((2.0 * dy) * dg)))
        imggen[y][x][b] = a * (((2.0 * py) * pb) if (py < 0.5) else (1.0 - ((2.0 * dy) * db)))
cv2.imwrite("gen.png", imggen)
print("Done!")
