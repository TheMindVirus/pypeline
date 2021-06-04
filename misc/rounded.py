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
frame = numpy.zeros([h, w, 3])
for x in range(0, w):
    px = x / w
    pr = math.cos(math.pi * ((px + 0.0) * 1.5)) if (px < 0.5) else math.cos(math.pi * ((1.0 - px) * 1.5))
    pg = math.cos(math.pi * ((px + 1.0) * 1.5)) if (px < (2.0 / 3.0)) else 0.0
    pb = math.cos(math.pi * ((px + 2.0) * 1.5)) if (px > (1.0 / 3.0)) else 0.0
    for y in range(0, h):
        py = 1.0 - (y / h)
        dy = 1.0 - py
        dr = 1.0 - pr
        dg = 1.0 - pg
        db = 1.0 - pb
        frame[y][x][r] = a * (((2.0 * py) * pr) if (py < 0.5) else (1.0 - ((2.0 * dy) * dr)))
        frame[y][x][g] = a * (((2.0 * py) * pg) if (py < 0.5) else (1.0 - ((2.0 * dy) * dg)))
        frame[y][x][b] = a * (((2.0 * py) * pb) if (py < 0.5) else (1.0 - ((2.0 * dy) * db)))
cv2.imwrite("frame.png", frame)
print("Done!")
