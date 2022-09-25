#pip3 install -U numpy
#pip3 install matplotlib
import math, random
import numpy as np
import matplotlib.pyplot as mpl

# TODO: Draw a Sphere with alpha 0.5 in matplotlib
#       Remove gridlines and Plot3D a line :D

def main():
    mpl.style.use("dark_background")
    data = []

    for i in range(0, 100):
        data.append(qubit())

    scope(data)
    mpl.show(block = False)

class qubit:
    def __init__(self, precision = 100):
        self.chroma = [random.random(), random.random(), random.random(), 0.5]
        self.position = [self.random(), self.random(), self.random()]
        self.thickness = random.random() * 3.0

    def random(self):
        return (random.random() * 2.0) - 1.0

def scope(data, scale_min = -1.0, scale_max = 1.0, scale_step = 1.0, precision = 100):
    figure = mpl.figure()
    grid = np.arange(scale_min, scale_max + scale_step, scale_step)
    
    axes = figure.add_subplot(1, 1, 1, projection = "3d")
    axes.set_title("Qubit Vector Engine")
    axes.axis("equal")
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
    u = np.linspace(0.0, np.pi, precision)
    v = np.linspace(0.0, 2.0 * np.pi, precision)
    x = np.outer(np.sin(u), np.sin(v))
    y = np.outer(np.sin(u), np.cos(v))
    z = np.outer(np.cos(u), np.ones_like(v))
    axes.plot_surface(x, y, z, cmap = "seismic", alpha = 0.1)
    for i in range(0, len(data)):
        x, y, z = data[i].position
        axes.plot3D(xs = [0.0, x], ys = [0.0, y], zs = [0.0, z],
                    color = data[i].chroma, linewidth = data[i].thickness)

if __name__ == "__main__":
    main()
