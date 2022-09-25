#pip3 install -U numpy
#pip3 install matplotlib
import math, random
import numpy as np
import matplotlib.pyplot as mpl

# Position xyz -1.0->1.0
# Projection xyz -1.0->1.0
# Cellular Metadata Influence

def main():
    mpl.style.use("dark_background")
    data = []

    data.append(trace())
    data[-1].label = "C(In)"
    data[-1].chroma = (1.00, 0.00, 0.35)

    data.append(trace())
    data[-1].label = "C(Out)"
    data[-1].chroma = (0.35, 1.00, 0.00)
    
    data.append(trace())
    data[-1].label = "C(Path)"
    data[-1].chroma = (0.00, 0.35, 1.00)
    data[-1].cell = data[-2].cell - data[-3].cell
    data[-1].graph = "plot"

    for i in range(0, 2):
        data = cast(data)

    scope(data)
    subplot(data)
    mpl.show(block = False)

class trace:
    def __init__(self):
        self.label = ""
        self.chroma = (random.random(), random.random(), random.random())
        self.cell = cell()
        self.graph = "scatter"

class path:
    def __init__(self):
        self.position = []
        self.projection = []
        side = random.randint(1, 6)
        for i in range(0, 3):
            self.position.append(self.random())
            self.projection.append(self.random())
            self.position[i] = 1.0 if side == (i * 2) + 1 else -1.0 if side == (i * 2) + 2 else self.position[i]
        self.metadata = str(self.random())

    def random(self):
        return (random.random() * 2.0) - 1.0

class cell:
    def __init__(self, n = 10):
        self.paths = []
        for i in range(0, n):
            self.paths.append(path())

    def __getitem__(self, index):
        return self.paths[index]
    
    def __setitem__(self, index, value):
        self.paths[index] = value

    def __sub__(self, previous):
        result = cell()
        for i in range(0, len(self.paths)):
            result[i].position = self.paths[i].position + previous.paths[i].position
            result[i].metadata = self.paths[i].metadata + previous.paths[i].metadata
            result[i].projection = self.paths[i].projection
        return result

    def calculate(self, previous):
        for i in range(0, len(self.paths)):
            for j in range(0, len(self.paths[i].position)): # turn this into an angle and collision
                self.paths[i].projection = self.paths[i].position[j] - previous.paths[i].position[j]
            print(self.paths[i].projection)

def cast(data):
    data.append(trace())
    data[-1].chroma = (1.00, 0.00, 0.35)
    data[-1].cell = data[-3].cell
    data.append(trace())
    data[-1].chroma = (0.35, 1.00, 0.00)
    data[-1].cell = data[-1].cell
    data[-1].cell.calculate(data[-2].cell) # calculate "projection from position" or "position from projection" here
    data.append(trace())
    data[-1].chroma = (0.00, 0.35, 1.00)
    data[-1].cell = data[-2].cell - data[-3].cell
    data[-1].graph = "plot"
    return data

def scope(data, scale_min = -1.0, scale_max = 1.0, scale_step = 1.0):
    figure = mpl.figure()
    grid = np.arange(scale_min, scale_max + scale_step, scale_step)
    
    axes = figure.add_subplot(1, 1, 1, projection = "3d")
    axes.set_title("Path Tracing Engine")
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
            for path in data[i].cell.paths:
                x1, y1, z1, x2, y2, z2 = path.position
                axes.plot3D(xs = [x1, x2], ys = [y1, y2], zs = [z1, z2], color = data[i].chroma, linewidth = 1)
        else:
            for path in data[i].cell.paths:
                x, y, z = path.position
                axes.scatter(x, y, z, color = data[i].chroma, marker = marker)

def subplot(data, scale_min = -1.0, scale_max = 1.0, scale_step = 1.0):
    figure = mpl.figure()
    grid = np.arange(scale_min, scale_max + scale_step, scale_step)
    subplots = len(data)
    
    for i in range(0, subplots):
        axes = figure.add_subplot(int(subplots / 3), 3, i + 1, projection = "3d")
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
            for path in data[i].cell.paths:
                x1, y1, z1, x2, y2, z2 = path.position
                axes.plot3D(xs = [x1, x2], ys = [y1, y2], zs = [z1, z2], color = data[i].chroma, linewidth = 1)
        else:
            for path in data[i].cell.paths:
                x, y, z = path.position
                axes.scatter(x, y, z, color = data[i].chroma, marker = "x")

if __name__ == "__main__":
    main()
