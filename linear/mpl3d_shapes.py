#pip3 install -U numpy
#pip3 install matplotlib
import math
import numpy as np
import matplotlib.pyplot as mpl
    
def main():
    mpl.style.use("dark_background")
    
    data = []

    data.append(record())
    data[-1].label = "circle"
    data[-1].aura = [1.0, 0.0, 0.3, 0.5]
    data[-1].formula = shapes().circle().check()
    
    data.append(record())
    data[-1].label = "triangle"
    data[-1].aura = [0.0, 1.0, 0.3, 0.5]
    data[-1].formula = shapes().triangle().check()

    data.append(record())
    data[-1].label = "cross"
    data[-1].aura = [0.3, 0.0, 1.0, 0.5]
    data[-1].formula = shapes().cross().check()

    data.append(record())
    data[-1].label = "square"
    data[-1].aura = [1.0, 1.0, 0.3, 0.5]
    data[-1].formula = shapes().square().check()
    
    scope(data)
    subplot(data)
    
    mpl.show(block = False)

class record:
    def __init__(self):
        self.label = ""
        self.aura = [1.0, 1.0, 1.0, 1.0]
        self.formula = 0

class shapes:
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

        self.origin_x = int((self.point_x + 0.5) / 2)
        self.origin_y = int((self.point_y + 0.5) / 2)
        self.origin_z = int((self.point_z + 0.5) / 2)
        
        for x in range(0, self.size_x):
            for y in range(0, self.size_y):
                for z in range(0, self.size_z):
                    self.voxels[x][y][z] = False

        self.iterator_x = range(1, self.point_x - 1)
        self.iterator_y = range(1, self.point_y - 1)
        self.iterator_z = range(1, self.point_z - 1)

        self.quadrant_x = range(self.origin_x, self.point_x - 1)
        self.quadrant_y = range(self.origin_y, self.point_y - 1)
        self.quadrant_z = range(self.origin_z, self.point_z - 1)

    def iterate(self, call, *args, **kwargs):
        for ix in self.iterator_x:
            for iy in self.iterator_y:
                for iz in self.iterator_z:
                    x = self.index_x[ix][iy][iz]
                    y = self.index_y[ix][iy][iz]
                    z = self.index_z[ix][iy][iz]
                    self.voxels[ix][iy][iz] = call(x, y, z, *args, **kwargs)
        return self

    def quadrant(self, call, *args, **kwargs):
        for mx in self.quadrant_x:
            for my in self.quadrant_y:
                for mz in self.quadrant_z:
                    x = self.index_x[mx][my][mz]
                    y = self.index_y[mx][my][mz]
                    z = self.index_z[mx][my][mz]
                    self.voxels[mx][my][mz] = call(x, y, z, *args, **kwargs)
        for ix in self.iterator_x:
            for iy in self.iterator_y:
                for iz in self.iterator_z:
                    ox = abs(ix - self.origin_x) + self.origin_x
                    oy = abs(iy - self.origin_y) + self.origin_y
                    oz = abs(iz - self.origin_z) + self.origin_z
                    if self.voxels[ox][oy][oz]:
                        self.voxels[ix][iy][iz] = True
        return self

    def circle(self, *args, **kwargs):
        def equation(x, y, z, r = 1.0, *args, **kwargs):
            return pow(-x, 2.0) + pow(-y, 2.0) + pow(-z, 2.0) <= pow(-r, 2.0)
        self.quadrant(equation, *args, **kwargs)
        return self

    def triangle(self, *args, **kwargs):
        def equation(x, y, z, u = 0.0, *args, **kwargs):
            return (((x + y) - 1) > u) and (((y + z) - 1) > u) and (((z + x) - 1) > u)
        self.quadrant(equation, *args, **kwargs)
        return self

    def cross(self, *args, **kwargs):
        def equation(x, y, z, t = 0.25, *args, **kwargs):
            return ((x - y) <= t) and ((y - z) <= t) and ((z - x) <= t)
        self.quadrant(equation, *args, **kwargs)
        return self

    def square(self, *args, **kwargs):
        def equation(x, y, z, s = 1.0, *args, **kwargs):
            return min(x, min(y, z)) <= s
        self.quadrant(equation, *args, **kwargs)
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
