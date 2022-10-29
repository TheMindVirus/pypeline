#pip3 install -U numpy
#pip3 install matplotlib
import numpy as np
import matplotlib.pyplot as mpl

SCALE_MIN = -2.0 * np.pi
SCALE_MAX =  2.0 * np.pi
SCALE_STEP = 64
SCALE_RANGE = SCALE_MAX - SCALE_MIN
 
def main():
    mpl.style.use("dark_background")
    data = []

    x = np.outer(np.linspace(SCALE_MIN, SCALE_MAX, SCALE_STEP), np.ones(SCALE_STEP))
    y = x.T #Transpose - Swap Axes

    data.append(record())
    data[-1].label = "Example"
    data[-1].surface = [x, y, np.sin(x ** 2) + np.cos(y ** 2)]
    data[-1].chroma = (1.0, 0.0, 0.0, 0.5)

    data.append(record())
    data[-1].label = "Terrain"
    data[-1].surface = [x, y, np.pi * (np.sin(x ** 2) + np.cos(y ** 2))]
    data[-1].chroma = (0.0, 0.0, 1.0, 0.5)

    surface(data)
    mpl.show(block = False)

class record:
    def __init__(self):
        pass

def surface(data, scale_min = SCALE_MIN, scale_max = SCALE_MAX, scale_range = SCALE_RANGE):
    figure = mpl.figure()
    grid = np.arange(scale_min, scale_max + scale_range, scale_range)
    
    axes = figure.add_subplot(1, 1, 1, projection = "3d")
    axes.set_title("Terrain")
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
        axes.grid(alpha = 0.5)
        axes.plot_surface(*(data[i].surface), color = data[i].chroma)

if __name__ == "__main__":
    main()
