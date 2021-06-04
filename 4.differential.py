#pip3 install opencv-python
#pip3 install -U numpy
import cv2, numpy
imgrgb = cv2.imread("rgb.png")
imgcmy = cv2.imread("cmy.png")
r = 2
g = 1
b = 0
w = len(imgrgb[0])
h = len(imgrgb)
imgdif = numpy.zeros([h, w, 3])
for x in range(0, w):
    for y in range(0, h):
        imgdif[y][x][r] = 0.0 if (abs(imgrgb[y][x][r] - imgcmy[y][x][r]) == 0) else 255.0
        imgdif[y][x][g] = 0.0 if (abs(imgrgb[y][x][g] - imgcmy[y][x][g]) == 0) else 255.0
        imgdif[y][x][b] = 0.0 if (abs(imgrgb[y][x][b] - imgcmy[y][x][b]) == 0) else 255.0
        
cv2.imwrite("dif.png", imgdif)
print("Done!")
