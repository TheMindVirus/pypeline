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
pr = 1.0
pg = 0.0
pb = 0.0
a = 255.0
state = 0
statelist = ["pg", "pr", "pb", "pg", "pr", "pb"]
inc = len(statelist) / w
frame = numpy.zeros([h, w, 3])
for x in range(0, w):
    px = x / w
    for y in range(0, h):
        py = 1.0 - (y / h)
        dy = 1.0 - py
        dr = 1.0 - pr
        dg = 1.0 - pg
        db = 1.0 - pb
        frame[y][x][r] = a * (((2.0 * py) * pr) if (py < 0.5) else (1.0 - ((2.0 * dy) * dr)))
        frame[y][x][g] = a * (((2.0 * py) * pg) if (py < 0.5) else (1.0 - ((2.0 * dy) * dg)))
        frame[y][x][b] = a * (((2.0 * py) * pb) if (py < 0.5) else (1.0 - ((2.0 * dy) * db)))
    state = int(px * len(statelist))
    exec(statelist[state] + " -= inc * (1.0 if (state % 2) else -1.0)")
cv2.imwrite("frame.png", frame)
print("Done!")
