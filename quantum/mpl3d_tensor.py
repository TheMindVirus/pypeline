#pip3 install -U numpy
#pip3 install matplotlib
import math, random
import numpy as np
import matplotlib.pyplot as mpl

# A = Live Data
# B = Model Data
# C = Actual Data
    
def main():
    mpl.style.use("dark_background")
    data = []

    data.append(record())
    data[-1].label = "T(Live)"
    data[-1].chroma = (1.0, 0.0, 0.0)

    data.append(record())
    data[-1].label = "T(Model)"
    data[-1].chroma = (1.0, 1.0, 0.0)
    
    data.append(record())
    data[-1].label = "T(Actual)"
    data[-1].graph = "plot"
    data[-1].tensor = data[-2].tensor - data[-3].tensor
    data[-1].chroma = (0.0, 1.0, 1.0)

    data.append(record())
    data[-1].chroma = (1.0, 0.7, 0.0)

    data.append(record())
    data[-1].chroma = (0.0, 1.0, 0.0)

    data.append(record())
    data[-1].graph = "plot"
    data[-1].tensor = data[-2].tensor - data[-3].tensor
    data[-1].chroma = (0.7, 0.0, 1.0)

    data.append(record())
    data[-1].chroma = (1.0, 1.0, 1.0)

    data.append(record())
    data[-1].chroma = (1.0, 0.7, 1.0)

    data.append(record())
    data[-1].graph = "plot"
    data[-1].tensor = data[-2].tensor - data[-3].tensor
    data[-1].chroma = (0.0, 0.3, 1.0)

    scope(data)
    subplot(data)
    mpl.show(block = False)

class record:
    def __init__(self):
        self.label = ""
        self.graph = "scatter"
        self.tensor = tensor()
        self.chroma = (1.0, 1.0, 1.0)

class tensor:
    def __init__(self, n = 10):
        self.data = []
        for i in range(0, n):
            self.data.append([random.random(), random.random(), random.random()])

    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value

    def __sub__(self, other):
        result = tensor()
        for i in range(0, len(self.data)):
            result[i] = self.data[i] + other[i]
        return result

def scope(data, scale_min = 0.0, scale_max = 1.0, scale_step = 0.5):
    figure = mpl.figure()
    grid = np.arange(scale_min, scale_max + scale_step, scale_step)
    
    axes = figure.add_subplot(1, 1, 1, projection = "3d")
    axes.set_title("Tensor Difference Engine")
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
        if (data[i].graph == "plot"):
            for x1, y1, z1, x2, y2, z2 in data[i].tensor:
                axes.plot3D(xs = [x1, x2], ys = [y1, y2], zs = [z1, z2], color = data[i].chroma, linewidth = 1)
        else:
            for x, y, z in data[i].tensor:
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
        if (data[i].graph == "plot"):
            for x1, y1, z1, x2, y2, z2 in data[i].tensor:
                axes.plot3D(xs = [x1, x2], ys = [y1, y2], zs = [z1, z2], color = data[i].chroma, linewidth = 1)
        else:
            for x, y, z in data[i].tensor:
                axes.scatter(x, y, z, color = data[i].chroma, marker = "x")

if __name__ == "__main__":
    main()
