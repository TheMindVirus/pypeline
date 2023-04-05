from PIL import Image
import numpy as np
#import cv2

img1 = Image.open("1316x575_1.png")
img2 = Image.open("1316x575_2.png")

#imgdiff = img2 - img1
img1_data = np.array(img1) #img1.getdata()
img2_data = np.array(img2) #img2.getdata()
img3 = img1.copy()
img3_data = img1_data.copy() #img3.getdata()
for i in range(0, img1.size[1]):
    for j in range(0, img1.size[0]):
        if i == 0 and j == 0:
            print(img1_data[i][j])
            print(img2_data[i][j])
        for k in range(0, img1_data[i][j].size):
            a = float(img1_data[i][j][k])
            b = float(img2_data[i][j][k])
            if a > b:
                a, b = [b, a]
            img3_data[i][j][k] = int(b - a)
        if i == 0 and j == 0:
            print(img3_data[i][j])
img3 = Image.fromarray(img3_data) #img3.setdata(img3_data)
img3.save("1316x575_3.png")

img4 = img1.copy()
img4_data = img1_data.copy()
for i in range(0, img1.size[1]):
    for j in range(0, img1.size[0]):
        avg1 = int((float(img1_data[i][j][0]) + float(img1_data[i][j][1]) + float(img1_data[i][j][2])) / 3)
        avg2 = int((float(img2_data[i][j][0]) + float(img2_data[i][j][1]) + float(img2_data[i][j][2])) / 3)
        if avg1 > avg2:
            avg1, avg2 = [avg2, avg1]
            diff = avg2 - avg1
            img4_data[i][j] = [diff, 0, int(float(diff * (0x44/0xFF)))]
        else:
            diff = avg2 - avg1
            img4_data[i][j] = [diff, diff, diff]
img4 = Image.fromarray(img4_data)
img4.save("1316x575_4.png")
