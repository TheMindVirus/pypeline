#pip3 install -U numpy
#pip3 install matplotlib
import math
import numpy as np
import matplotlib.pyplot as mpl
    
def main():
    mpl.style.use("dark_background")
    
    data = []
    misc = []

    data.append(record())
    data[-1].label = "linear"
    data[-1].aura = [1.0, 0.0, 0.3, 1.0]
    data[-1].formula = lineariser().linear().check()
    
    data.append(record())
    data[-1].label = "triangular"
    data[-1].aura = [1.0, 1.0, 0.0, 1.0]
    data[-1].formula = lineariser().triangular().check()
    
    data.append(record())
    data[-1].label = "quadratic"
    data[-1].aura = [0.0, 1.0, 1.0, 1.0]
    data[-1].formula = lineariser().quadratic().check()

    data.append(record())
    data[-1].label = "elliptical"
    data[-1].aura = [0.0, 0.0, 1.0, 1.0]
    data[-1].formula = lineariser().elliptical().check()

    data.append(record())
    data[-1].label = "spherical"
    data[-1].aura = [1.0, 0.7, 0.0, 1.0]
    data[-1].formula = lineariser().spherical().check()

    data.append(record())
    data[-1].label = "conical"
    data[-1].aura = [0.0, 1.0, 0.0, 1.0]
    data[-1].formula = lineariser().conical().check()

    data.append(record())
    data[-1].label = "parabolic"
    data[-1].aura = [0.7, 0.0, 1.0, 1.0]
    data[-1].formula = lineariser().parabolic().check()

    data.append(record())
    data[-1].label = "hyperbolic"
    data[-1].aura = [1.0, 1.0, 1.0, 1.0]
    data[-1].formula = lineariser().hyperbolic().check()

    data.append(record())
    data[-1].label = "radiocubic"
    data[-1].aura = [1.0, 0.7, 1.0, 1.0]
    data[-1].formula = lineariser().radiocubic().check()
    
    scope(data)
    subplot(data)

    misc.append(record())
    misc[-1].label = "cubic"
    misc[-1].aura = [1.0, 0.0, 0.3, 1.0]
    misc[-1].formula = lineariser().cubic().check()
    
    misc.append(record())
    misc[-1].label = "bicubic"
    misc[-1].aura = [1.0, 1.0, 0.0, 1.0]
    misc[-1].formula = lineariser().bicubic().check()
    
    misc.append(record())
    misc[-1].label = "trilinear"
    misc[-1].aura = [0.0, 1.0, 1.0, 1.0]
    misc[-1].formula = lineariser().trilinear().check()

    misc.append(record())
    misc[-1].label = "lanczos"
    misc[-1].aura = [0.0, 0.0, 1.0, 1.0]
    misc[-1].formula = lineariser().lanczos().check()

    misc.append(record())
    misc[-1].label = "laplacian"
    misc[-1].aura = [1.0, 0.7, 0.0, 1.0]
    misc[-1].formula = lineariser().laplacian().check()

    misc.append(record())
    misc[-1].label = "gaussian"
    misc[-1].aura = [0.0, 1.0, 0.0, 1.0]
    misc[-1].formula = lineariser().gaussian().check()

    misc.append(record())
    misc[-1].label = "butterworth"
    misc[-1].aura = [0.7, 0.0, 1.0, 1.0]
    misc[-1].formula = lineariser().butterworth().check()

    misc.append(record())
    misc[-1].label = "chebyshev"
    misc[-1].aura = [1.0, 1.0, 1.0, 1.0]
    misc[-1].formula = lineariser().chebyshev().check()

    misc.append(record())
    misc[-1].label = "bessel"
    misc[-1].aura = [1.0, 0.7, 1.0, 1.0]
    misc[-1].formula = lineariser().bessel().check()
    
    scope(misc)
    subplot(misc)
    
    mpl.show(block = False)

class record:
    def __init__(self):
        self.label = ""
        self.aura = [1.0, 1.0, 1.0, 1.0]
        self.formula = 0

class lineariser:
    def __init__(self, number_x = 4, number_y = 4, number_z = 4):
        self.number_x = number_x
        self.number_y = number_y
        self.number_z = number_z
        
        self.actual_x = self.number_x + 1
        self.actual_y = self.number_y + 1
        self.actual_z = self.number_z + 1
        
        self.size_x = self.actual_x * 2
        self.size_y = self.actual_y * 2
        self.size_z = self.actual_z * 2

        self.point_x = self.size_x + 1
        self.point_y = self.size_y + 1
        self.point_z = self.size_z + 1
        
        self.voxels = np.ndarray((self.size_x, self.size_y, self.size_z), dtype = bool)
        self.index_x, self.index_y, self.index_z = np.indices((self.point_x, self.point_y, self.point_z))

        self.index_x = ((self.index_x - self.actual_x) / self.number_x)
        self.index_y = ((self.index_y - self.actual_y) / self.number_y)
        self.index_z = ((self.index_z - self.actual_z) / self.number_z)
        
        for x in range(0, self.size_x):
            for y in range(0, self.size_y):
                for z in range(0, self.size_z):
                    self.voxels[x][y][z] = False

        self.iterator_x = range(1, self.point_x - 1)
        self.iterator_y = range(1, self.point_y - 1)
        self.iterator_z = range(1, self.point_z - 1)

    def iterate(self, call, *args, **kwargs):
        for ix in self.iterator_x:
            for iy in self.iterator_y:
                for iz in self.iterator_z:
                    x = self.index_x[ix][iy][iz]
                    y = self.index_y[ix][iy][iz]
                    z = self.index_z[ix][iy][iz]
                    self.voxels[ix][iy][iz] = call(x, y, z, *args, **kwargs)
        return self

    def linear(self):
        def equation(x, y, z):
            return x == y == z
        self.iterate(equation)
        return self

    def triangular(self):
        def equation(x, y, z):
            return pow(x, 2) + pow(y, 2) == pow(z, 2)
        self.iterate(equation)
        return self

    def quadratic(self):
        def equation(x, y, z):
            result = False
            if x == 0:
                return False
            if 0 == (-y + math.sqrt(abs(pow(y, 2) - (4 * x * z))) / (2 * x)):
                result = True
            if 0 == (-y - math.sqrt(abs(pow(y, 2) - (4 * x * z))) / (2 * x)):
                result = True
            return result
        self.iterate(equation)
        return self

    def elliptical(self, a = 0, b = 0, r = 1):
        def equation(x, y, z, a, b, r):
            return pow(a - x, 2) + pow(b - y, 2) < pow(r, 2)
        self.iterate(equation, a = a, b = b, r = r)
        return self

    def spherical(self, a = 0, b = 0, c = 0, r = 1):
        def equation(x, y, z):
            return pow(a - x, 2) + pow(b - y, 2) + pow(c - z, 2) < pow(r, 2)
        self.iterate(equation)
        return self

    def conical(self, a = 0, b = 0, c = 0):
        def equation(x, y, z, a, b, c):
            return pow(a - x, 2) + pow(b - y, 2) < pow(c - z, 2)
        self.iterate(equation, a = a, b = b, c = c)
        return self

    def parabolic(self, c = -1):
        def equation(x, y, z, c):
            return y > pow(x, 2) + c
        self.iterate(equation, c = c)
        return self

    def hyperbolic(self):
        def equation(x, y, z):
            return (pow(x, 2) - pow(y, 2)) < 1
        self.iterate(equation)
        return self

    def radiocubic(self, a = 1, b = 1, c = 1):
        def equation(x, y, z, a, b, c):
            if x == 0 or y == 0 or z == 0:
                return False
            return 1 < math.atan(math.sqrt(abs(pow(a, 2) + pow(math.tan(x) * b, 2) + pow(math.tan(x) * c, 2)))) / math.atan(1 / 1)
        self.iterate(equation, a = a, b = b, c = c)
        return self

    def cubic(self):
        def equation(x, y, z):
            return y > pow(x, 3)
        self.iterate(equation)
        return self

    def bicubic(self):
        def equation(x, y, z):
            return z > pow(x, 3) * pow(y, 3)
        self.iterate(equation)
        return self

    def trilinear(self, a = 0, b = 0, c = 0, t = 0):
        def equation(x, y, z, a, b, c, t):
            return (x - math.cos(t * a)) + (y - math.cos(t * b)) + (z - math.cos(t * c))
        self.iterate(equation, a = a, b = b, c = c, t = t)
        return self

    def lanczos(self):
        def equation(x, y, z):
            if x == 0:
                return False
            return y > math.sin(x) / x
        self.iterate(equation)
        return self

    def laplacian(self, d = 1, v = 2):
        def equation(x, y, z, d, v):
            if d == 0 \
            or pow(x, 2) == 0 \
            or pow(y, 2) == 0 \
            or pow(z, 2) == 0:
                return True
            return v < math.sqrt(abs((pow(d, 2) / (d * pow(x, 2))) + (pow(d, 2) / (d * pow(y, 2))) + (pow(d, 2) / (d * pow(z, 2)))))
        self.iterate(equation, d = d, v = v)
        return self

    def gaussian(self, b = 10):
        def equation(x, y, z, b):
            return 1 < pow(b, pow(-x, 2))
        self.iterate(equation, b = b)
        return self

    def butterworth(self, t = 1):
        def equation(x, y, z, t):
            return x / math.sin(t)
        self.iterate(equation, t = t)
        return self

    def chebyshev(self):
        def equation(x, y, z):
            if pow(x, 2) == 0:
                return False
            if math.sqrt(abs(1 + (1 / pow(x, 2)))) == 0:
                return False
            return -1 / math.sqrt(abs(1 + (1 / pow(x, 2))))
        self.iterate(equation)
        return self

    def bessel(self, a = 1, b = 1, c = 1, d = 1):
        def equation(x, y, z, a, b, c, d):
            if math.sqrt(abs(a * pow(x, 3) + b * pow(x, 2) + c * pow(x, 1) + d * pow(x, 0))) == 0:
                return False
            return 1 / math.sqrt(abs(a * pow(x, 3) + b * pow(x, 2) + c * pow(x, 1) + d * pow(x, 0)))
        self.iterate(equation, a = a, b = b, c = c, d = d)
        return self

    def check(self):
        self.half_x = 1.0 / (2.0 * self.number_x)
        self.half_y = 1.0 / (2.0 * self.number_y)
        self.half_z = 1.0 / (2.0 * self.number_z)

        self.x = self.index_x - self.half_x
        self.y = self.index_y - self.half_y
        self.z = self.index_z - self.half_z
        return self

def scope(data, scale_min = -1.0, scale_max = 1.0, scale_step = 0.5):
    figure = mpl.figure()
    
    axes = figure.add_subplot(1, 1, 1, projection = "3d")
    axes.set_title("scope")
    axes.set(xlabel = "x", ylabel = "y", zlabel = "z")
    axes.xaxis.set_ticks(np.arange(-1.000001, 1.000001, 0.5))
    axes.yaxis.set_ticks(np.arange(-1.000001, 1.000001, 0.5))
    axes.zaxis.set_ticks(np.arange(-1.000001, 1.000001, 0.5))
    axes.set_xlim((-1.5, 1.5))
    axes.set_ylim((-1.5, 1.5))
    axes.set_zlim((-1.5, 1.5))
    axes.set_aspect("equal")
    axes.xaxis.pane.fill = False
    axes.yaxis.pane.fill = False
    axes.zaxis.pane.fill = False

    for i in range(0, len(data)):
        axes.voxels(data[i].formula.x, data[i].formula.y, data[i].formula.z,
                    data[i].formula.voxels, facecolors = data[i].aura,
                    linewidth = 0)

def subplot(data, scale_min = -1.0, scale_max = 1.0, scale_step = 0.5):
    figure = mpl.figure()
    subplots = int(math.sqrt(len(data)))
    
    for i in range(0, len(data)):
        axes = figure.add_subplot(subplots, subplots, i + 1, projection = "3d")
        axes.set_title(data[i].label)
        axes.set(xlabel = "x", ylabel = "y", zlabel = "z")
        axes.xaxis.set_ticks(np.arange(-1.000001, 1.000001, 0.5))
        axes.yaxis.set_ticks(np.arange(-1.000001, 1.000001, 0.5))
        axes.zaxis.set_ticks(np.arange(-1.000001, 1.000001, 0.5))
        axes.set_xlim((-1.5, 1.5))
        axes.set_ylim((-1.5, 1.5))
        axes.set_zlim((-1.5, 1.5))
        axes.set_aspect("equal")
        axes.xaxis.pane.fill = False
        axes.yaxis.pane.fill = False
        axes.zaxis.pane.fill = False
        axes.voxels(data[i].formula.x, data[i].formula.y, data[i].formula.z,
                    data[i].formula.voxels, facecolors = data[i].aura,
                    linewidth = 0)

if __name__ == "__main__":
    main()
