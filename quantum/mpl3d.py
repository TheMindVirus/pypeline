#pip3 install -U numpy
#pip3 install matplotlib
import math
import numpy as np
import matplotlib.pyplot as mpl
    
def main():
    mpl.style.use("dark_background")
    data = []

    data.append(record())
    data[-1].label = "P(A)"
    data[-1].matrix = matrix().clamp().check()
    data[-1].chroma = (1.0, 0.0, 0.0)
    data[-1].marker = "x"

    data.append(record())
    data[-1].label = "P(B)"
    data[-1].matrix = matrix().clamp(1).check()
    data[-1].chroma = (1.0, 1.0, 0.0)
    data[-1].marker = "x"
    
    data.append(record())
    data[-1].label = "avg(P(A), P(B))"
    data[-1].matrix = matrix().canon().check()
    data[-1].chroma = (0.0, 1.0, 1.0)
    data[-1].marker = "x"

    data.append(record())
    data[-1].label = "P(A|B)"
    data[-1].matrix = matrix().carve(1).check()
    data[-1].chroma = (1.0, 0.7, 0.0)
    data[-1].marker = "x"

    data.append(record())
    data[-1].label = "P(B|A)"
    data[-1].matrix = matrix().carve().check()
    data[-1].chroma = (0.0, 1.0, 0.0)
    data[-1].marker = "x"

    data.append(record())
    data[-1].label = "P(1)"
    data[-1].matrix = matrix().clear(1).check()
    data[-1].chroma = (0.7, 0.0, 1.0)
    data[-1].marker = "x"

    data.append(record())
    data[-1].label = "P(AuB)"
    data[-1].chroma = (1.0, 1.0, 1.0)
    data[-1].matrix = matrix().count().check()
    data[-1].marker = "x"

    data.append(record())
    data[-1].label = "P(AnB)"
    data[-1].chroma = (1.0, 0.7, 1.0)
    data[-1].matrix = matrix().cross().check()
    data[-1].marker = "x"

    data.append(record())
    data[-1].label = "P(0)"
    data[-1].chroma = (0.3, 0.3, 1.0)
    data[-1].matrix = matrix().clear().check()
    data[-1].marker = "x"

    scope(data)
    subplot(data)
    mpl.show(block = False)

class record:
    def __init__(self):
        self.label = ""
        self.matrix = matrix().check()
        self.chroma = (1.0, 1.0, 1.0)
        self.marker = "x"

class matrix:
    def __init__(self, scale_min = 0.0, scale_max = 1.0, scale_step = 0.1):
        precision = int((scale_max - scale_min) / scale_step)
        self.X = np.linspace(scale_min, scale_max, precision)
        self.Y = [[0.5, 0.5, 0.5]]

    def clear(self, value = 0.0):
        self.Y = []
        size = len(self.X)
        for x in range(0, size):
            for y in range(0, size):
                self.Y.append([self.X[x], self.X[y], value])
        return self

    def clamp(self, flip = 0):
        self.Y = []
        size = len(self.X)
        for x in range(0, size):
            for y in range(0, size):
                self.Y.append([self.X[x], self.X[y], self.X[y if flip else x]])
        return self

    def canon(self):
        self.Y = []
        size = len(self.X)
        for x in range(0, size):
            for y in range(0, size):
                self.Y.append([self.X[x], self.X[y], (self.X[x] + self.X[y]) / 2.0])
        return self

    def count(self, flip = 0):
        self.Y = []
        size = len(self.X)
        for x in range(0, size):
            for y in range(0, size):
                a = y if flip else x
                b = x if flip else y
                value = (self.X[a] + self.X[b]) - (self.X[a] * self.X[b])
                self.Y.append([self.X[x], self.X[y], value])
        return self

    def cross(self):
        self.Y = []
        size = len(self.X)
        for x in range(0, size):
            for y in range(0, size):
                self.Y.append([self.X[x], self.X[y], self.X[x] * self.X[y]])
        return self

    def carve(self, flip = 0):
        self.Y = []
        size = len(self.X)
        for x in range(0, size):
            for y in range(0, size):
                a = y if flip else x
                b = x if flip else y
                value = (self.X[a] * self.X[b]) / (self.X[b] if self.X[b] != 0.0 else 1.0)
                self.Y.append([self.X[x], self.X[y], value if self.X[b] != 0.0 else self.X[a]])
        return self

    def check(self):
        return self.Y

def scope(data, scale_min = 0.0, scale_max = 1.0, scale_step = 0.5):
    figure = mpl.figure()
    grid = np.arange(scale_min, scale_max + scale_step, scale_step)
    
    axes = figure.add_subplot(1, 1, 1, projection = "3d")
    axes.set_title("scope")
    axes.set(xlabel = "x", ylabel = "y", zlabel = "z")
    axes.set(xlim = (scale_min, scale_max))
    axes.set(ylim = (scale_min, scale_max))
    axes.set(zlim = (scale_min, scale_max))
    axes.xaxis.set_ticks(grid)
    axes.yaxis.set_ticks(grid)
    axes.zaxis.set_ticks(grid)
    axes.xaxis.pane.fill = False
    axes.yaxis.pane.fill = False
    axes.zaxis.pane.fill = False

    for i in range(0, len(data)):
        marker = data[i].marker if hasattr(data[i], "marker") else "x"
        axes.grid(alpha = 0.5)
        for x, y, z in data[i].matrix:
            axes.scatter(x, y, z, color = data[i].chroma, marker = marker)

def subplot(data, scale_min = 0.0, scale_max = 1.0, scale_step = 0.5):
    figure = mpl.figure()
    grid = np.arange(scale_min, scale_max + scale_step, scale_step)
    subplots = int(math.sqrt(len(data)))
    
    for i in range(0, len(data)):
        axes = figure.add_subplot(subplots, subplots, i + 1, projection = "3d")
        axes.set_title(data[i].label)
        axes.set(xlabel = "x", ylabel = "y", zlabel = "z")
        axes.set(xlim = (scale_min, scale_max))
        axes.set(ylim = (scale_min, scale_max))
        axes.set(zlim = (scale_min, scale_max))
        axes.xaxis.set_ticks(grid)
        axes.yaxis.set_ticks(grid)
        axes.zaxis.set_ticks(grid)
        axes.xaxis.pane.fill = False
        axes.yaxis.pane.fill = False
        axes.zaxis.pane.fill = False
        axes.grid(alpha = 0.5)
        for x, y, z in data[i].matrix:
            axes.scatter(x, y, z, color = data[i].chroma, marker = "x")

if __name__ == "__main__":
    main()
