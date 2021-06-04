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
imgcrs = numpy.zeros([h, w, 3])

#def circular(i):
#    return (numpy.sqrt(1.0 - pow((i - 1.0), 2)) if i > 0.0 else 0.0)

def circular(i):
    return (numpy.sqrt(1.0 - pow((i - 1.0) * 2.0, 2)) + 1.0) * 0.5 if i > 0.5 else (-1.0 * numpy.sqrt(1.0 - pow(i * 2.0, 2))) * 0.5 + 0.5 if i > 0.0 else 0.0

for x in range(0, w):
    px = x / w
    if (px <= (1.0 / 6.0)):
        pxx = px
        pr = 1.0
        pg = circular(pxx * 6.0)
        pb = 0.0
    elif (px <= (2.0 / 6.0)):
        pxx = px - (1.0 / 6.0)
        pr = 1.0 - circular(pxx * 6.0)
        pg = 1.0
        pb = 0.0
    elif (px <= (3.0 / 6.0)):
        pxx = px - (2.0 / 6.0)
        pr = 0.0
        pg = 1.0
        pb = circular(pxx * 6.0)
    elif (px <= (4.0 / 6.0)):
        pxx = px - (3.0 / 6.0)
        pr = 0.0
        pg = 1.0 - circular(pxx * 6.0)
        pb = 1.0
    elif (px <= (5.0 / 6.0)):
        pxx = px - (4.0 / 6.0)
        pr = circular(pxx * 6.0)
        pg = 0.0
        pb = 1.0
    else:
        pxx = px - (5.0 / 6.0)
        pr = 1.0
        pg = 0.0
        pb = 1.0 - circular(pxx * 6.0)
    for y in range(0, h):
        py = 1.0 - (y / h)
        imgcrs[y][x][r] = 255.0 if (py <= pr) else 0.0
        imgcrs[y][x][g] = 255.0 if (py <= pg) else 0.0
        imgcrs[y][x][b] = 255.0 if (py <= pb) else 0.0
cv2.imwrite("crs.png", imgcrs)
print("Done!")
