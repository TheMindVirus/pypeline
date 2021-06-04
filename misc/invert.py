#pip3 install opencv-python
#pip3 install -U numpy
import cv2
img = cv2.imread("input.png")
newimg = img.copy()
r = 2
g = 1
b = 0
for y in range(0, len(img)):
    for x in range(0, len(img[y])):
        newimg[y][x][r] = 255 - img[y][x][r]
        newimg[y][x][g] = 255 - img[y][x][g]
        newimg[y][x][b] = 255 - img[y][x][b]
cv2.imwrite("output.png", newimg)
print("Done!")
