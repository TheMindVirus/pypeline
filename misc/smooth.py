#pip3 install opencv-python
#pip3 install -U numpy
import cv2, numpy, math
img = cv2.imread("crs.png")
R = 2
G = 1
B = 0
w = len(img[0])
h = len(img)
cx = w / 2
cy = h / 2

#img = numpy.zeros([h, w, 3])
#img[500][500][G] = 255.0

overspill = math.pi / 8.0
#imgavg = img.copy()
imgavg = numpy.zeros([h, w, 3])

"""
for x in range(0, w):
    for y in range(0, h):
        d = min(max(y + 1, 0), h - 1)
        u = min(max(y - 1, 0), h - 1)
        r = min(max(x + 1, 0), w - 1)
        l = min(max(x - 1, 0), w - 1)
        imgavg[y][x][R] = img[y][x][R] + (overspill * max(
                          img[d][x][R],
                          img[u][x][R],
                          img[y][r][R],
                          img[y][l][R]))
        imgavg[y][x][G] = img[y][x][G] + (overspill * max(
                          img[d][x][G],
                          img[u][x][G],
                          img[y][r][G],
                          img[y][l][G]))
        imgavg[y][x][B] = img[y][x][B] + (overspill * max(
                          img[d][x][B],
                          img[u][x][B],
                          img[y][r][B],
                          img[y][l][B]))
"""

"""
rfft = numpy.fft.fft2(numpy.fft.fftshift(img[:,:,R]))
gfft = numpy.fft.fft2(numpy.fft.fftshift(img[:,:,G]))
bfft = numpy.fft.fft2(numpy.fft.fftshift(img[:,:,B]))
for i in range(0, len(rfft)):
    for j in range(0, len(rfft[0])):
        rfft[i][j] = rfft[i][j] if (rfft[i][j] > 0.9) else 0.0
        gfft[i][j] = gfft[i][j] if (gfft[i][j] > 0.9) else 0.0
        bfft[i][j] = bfft[i][j] if (bfft[i][j] > 0.9) else 0.0
imgavg[:,:,R] = numpy.real(numpy.fft.ifftshift(numpy.fft.ifft2(rfft)))
imgavg[:,:,G] = numpy.real(numpy.fft.ifftshift(numpy.fft.ifft2(gfft)))
imgavg[:,:,B] = numpy.real(numpy.fft.ifftshift(numpy.fft.ifft2(bfft)))
"""

def circular(i):
    return ((numpy.sqrt(1.0 - pow((i - 1.0) * 2.0, 2)) + 1.0) * 0.5 if i > 0.5 else (-1.0 * numpy.sqrt(1.0 - pow(i * 2.0, 2)) + 0.0) * 0.5 + 0.5 if i > 0.0 else 0)

#"""
rfft = numpy.fft.fft2(numpy.fft.fftshift(img[:,:,R]))
gfft = numpy.fft.fft2(numpy.fft.fftshift(img[:,:,G]))
bfft = numpy.fft.fft2(numpy.fft.fftshift(img[:,:,B]))
for x in range(0, w):
    px = x / w
    for y in range(0, h):
        py = 1.0 - (y / h)
        f1 = 0.6
        f2 = 0.7
        f3 = f2 - f1
        I = math.sqrt(pow(px - 0.5, 2) + pow(py - 0.5, 2))
        #I = 0.0 if I < f1 else 1.0 if I > f2 else math.sqrt(1.0 - pow((I - f2) / f3, 2)) - f1
        I = 0.0 if I < f1 else 1.0 if I > f2 else circular((I - f1) / f3)
        #I = 1.0 - I
        rfft[y][x] *= I
        gfft[y][x] *= I
        bfft[y][x] *= I
imgavg[:,:,R] = numpy.real(numpy.fft.ifftshift(numpy.fft.ifft2(rfft)))
imgavg[:,:,G] = numpy.real(numpy.fft.ifftshift(numpy.fft.ifft2(gfft)))
imgavg[:,:,B] = numpy.real(numpy.fft.ifftshift(numpy.fft.ifft2(bfft)))
#"""

"""
for x in range(0, w):
    px = x / w
    for y in range(0, h):
        py = 1.0 - (y / h)
        f1 = 0.2
        f2 = 0.5
        f3 = f2 - f1
        I = math.sqrt(pow(px - 0.5, 2) + pow(py - 0.5, 2))
        #I = 0.0 if I < f1 else 1.0 if I > f2 else math.sqrt(1.0 - pow((I - f2) / f3, 2)) - f1
        I = 0.0 if I < f1 else 1.0 if I > f2 else circular((I - f1) / f3)
        imgavg[y][x][R] = 255.0 * I
"""

cv2.imwrite("avg.png", imgavg)
print("Done!")
