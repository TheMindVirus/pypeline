#pip3 install -U numpy
#pip3 install matplotlib
import math
import numpy as np
import matplotlib.pyplot as mpl
    
def main():
    mpl.style.use("dark_background")
    
    data = []
    
    data.append(particle())
    data[-1].aura = [0.75, 0.25, 0.25, 0.5]
    data[-1].formula = shapes().circle()

    data.append(particle())
    data[-1].aura = [0.25, 0.75, 0.25, 0.5]
    data[-1].formula = shapes().triangle()

    data.append(particle())
    data[-1].aura = [0.25, 0.25, 0.75, 0.5]
    data[-1].formula = shapes().square() - (shapes().circle() + shapes().triangle())
    
    data.append(particle())
    data[-1].aura = [0.75, 0.75, 0.75, 0.5]
    data[-1].formula = shapes().circle() + shapes().triangle() + (shapes().square() - (shapes().circle() + shapes().triangle()))

    subplot(particle.matrix(data))

    misc = []

    misc.append(particle())
    misc[-1].aura = [1.0, 0.0, 0.0, 0.5]
    misc[-1].formula = shapes().circle()

    misc.append(particle())
    misc[-1].aura = [0.0, 1.0, 0.0, 0.5]
    misc[-1].formula = shapes().triangle()

    misc.append(particle())
    misc[-1].aura = [0.0, 0.0, 1.0, 0.5]
    misc[-1].formula = shapes().cross()
    
    misc.append(particle())
    misc[-1].aura = [1.0, 1.0, 1.0, 0.5]
    misc[-1].formula = shapes().square()
    
    subplot(particle.matrix(misc))
    
    mpl.show(block = False)

class particle:
    def __init__(self):
        self.aura = [1.0, 1.0, 1.0, 1.0]
        self.formula = shapes()
        
    def __repr__(self):
        _new = particle()
        _new.aura = self.aura
        _new.formula = shapes()
        _new.formula.voxels = self.formula.voxels.copy()
        return _new #self

    def __xor__(self, other):
        _new = particle()
        _new.aura = \
        [
            (self.aura[0] * 0.5) + (other.aura[0] * 0.5),
            (self.aura[1] * 0.5) + (other.aura[1] * 0.5),
            (self.aura[2] * 0.5) + (other.aura[2] * 0.5),
            (self.aura[3] * 0.5) + (other.aura[3] * 0.5),
        ]
        _new.formula = shapes()
        _new.formula.voxels = self.formula.voxels.copy()
        _new.formula.voxels = _new.formula.voxels ^ other.formula.voxels
        return _new #self

    def invert(self):
        _new = particle()
        _new.aura = \
        [
            (1.0 - self.aura[0]),
            (1.0 - self.aura[1]),
            (1.0 - self.aura[2]),
            (1.0 - self.aura[3]),
        ]
        _new.formula = self.formula.invert()
        return _new #self

    def matrix(data):
        misc = data[:]
        mat = []
        sz = len(misc)
        blank = particle()
        for y in range(sz, -sz -1, -1):
            for x in range(-sz, sz + 1):
                idx = abs(x)
                idy = abs(y)
                if idx == 0:
                    idx = idy
                if idy == 0:
                    idy = idx
                xraw = blank.__repr__()
                yraw = blank.__repr__()
                if idx > 0:
                    xraw = misc[idx - 1].__repr__() # !!! not called !!! #
                    #raw.formula.voxels = misc[idx - 1].formula.voxels.copy()
                if idy > 0:
                    yraw = misc[idy - 1].__repr__()
                if x < 0 or (x == 0 and y < 0):
                    xraw = xraw.invert()
                if y < 0 or (y == 0 and x < 0):
                    yraw = yraw.invert()
                raw = xraw
                if x != 0 and y != 0: # and x != y:
                    raw = xraw ^ yraw
                mat.append(raw)
        return mat

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

        self._check()

    def __add__(self, other):
        for ix in self.iterator_x:
            for iy in self.iterator_y:
                for iz in self.iterator_z:
                    x = self.index_x[ix][iy][iz]
                    y = self.index_y[ix][iy][iz]
                    z = self.index_z[ix][iy][iz]
                    self.voxels[ix][iy][iz] |= other.voxels[ix][iy][iz]
        return self

    def __sub__(self, other):
        for ix in self.iterator_x:
            for iy in self.iterator_y:
                for iz in self.iterator_z:
                    x = self.index_x[ix][iy][iz]
                    y = self.index_y[ix][iy][iz]
                    z = self.index_z[ix][iy][iz]
                    self.voxels[ix][iy][iz] &= not other.voxels[ix][iy][iz]
        return self

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

    def invert(self, *args, **kwargs):
        for ix in self.iterator_x:
            for iy in self.iterator_y:
                for iz in self.iterator_z:
                    x = self.index_x[ix][iy][iz]
                    y = self.index_y[ix][iy][iz]
                    z = self.index_z[ix][iy][iz]
                    self.voxels[ix][iy][iz] = not self.voxels[ix][iy][iz]
        return self

    def circle(self, *args, **kwargs):
        def equation(x, y, z, r = 1.05, *args, **kwargs):
            return pow(-x, 2.0) + pow(-y, 2.0) + pow(-z, 2.0) <= pow(-r, 2.0)
        self.quadrant(equation, *args, **kwargs)
        self._check()
        return self

    def triangle(self, *args, **kwargs):
        def equation(x, y, z, u = 0.00, *args, **kwargs):
            return (((x + y) - 1.0) > u) and (((y + z) - 1.0) > u) and (((z + x) - 1.0) > u)
        self.quadrant(equation, *args, **kwargs)
        self._check()
        return self

    def cross(self, *args, **kwargs):
        def equation(x, y, z, t = 0.25, *args, **kwargs):
            return (abs(x - y) <= t) and (abs(y - z) <= t) and (abs(z - x) <= t)
        self.quadrant(equation, *args, **kwargs)
        self._check()
        return self

    def square(self, *args, **kwargs):
        def equation(x, y, z, s = 1.0, *args, **kwargs):
            return min(x, min(y, z)) <= s
        self.quadrant(equation, *args, **kwargs)
        self._check()
        return self

    def _check(self):
        self.half_x = 1.0 / (2.0 * self.number_x)
        self.half_y = 1.0 / (2.0 * self.number_y)
        self.half_z = 1.0 / (2.0 * self.number_z)

        self.x = self.index_x - self.half_x
        self.y = self.index_y - self.half_y
        self.z = self.index_z - self.half_z
        return self

def subplot(data, scale_min = -1.0, scale_max = 1.0, scale_step = 0.5):
    figure = mpl.figure()
    subplots = int(math.sqrt(len(data)))
    
    for i in range(0, len(data)):
        axes = figure.add_subplot(subplots, subplots, i + 1, projection = "3d")
        axes.xaxis.set_ticks(np.arange(1, 1, 1))
        axes.yaxis.set_ticks(np.arange(1, 1, 1))
        axes.zaxis.set_ticks(np.arange(1, 1, 1))
        axes.set_xlim((-1.5, 1.5))
        axes.set_ylim((-1.5, 1.5))
        axes.set_zlim((-1.5, 1.5))
        axes.set_axis_off()
        axes.set_aspect("equal")
        axes.voxels(data[i].formula.x, data[i].formula.y, data[i].formula.z,
                    data[i].formula.voxels, facecolors = data[i].aura,
                    linewidth = 0)

if __name__ == "__main__":
    main()
