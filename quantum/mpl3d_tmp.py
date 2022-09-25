#pip3 install -U numpy
#pip3 install matplotlib
import math
import random
import numpy as np
import matplotlib.pyplot as mpl

mpl.style.use("dark_background")
figure = mpl.figure()
gmin = 0.0
gmax = 1.0
grid = np.arange(gmin, gmax + 0.5, 0.5)
axes = figure.add_subplot(projection = "3d")

axes.set_title("scope")
axes.set(xlabel = "x", ylabel = "y", zlabel = "z")
axes.set(xlim = [-0.1, 1.1], ylim = [-0.1, 1.1], zlim = [-0.1, 1.1])
axes.xaxis.set_ticks(grid)
axes.yaxis.set_ticks(grid)
axes.zaxis.set_ticks(grid)
axes.xaxis.pane.fill = False
axes.yaxis.pane.fill = False
axes.zaxis.pane.fill = False
axes.grid(alpha = 0.5)

for i in range(0, 100):
    x = random.uniform(gmin, gmax)
    y = random.uniform(gmin, gmax)
    z = random.uniform(gmin, gmax)
    axes.scatter(x, y, z, marker = "x", color = (1.0, 0.0, 0.3))

mpl.show(block = False)
