#pip3 install -U numpy
#pip3 install matplotlib
import math
import numpy as np
import matplotlib.pyplot as mpl

TITLE = "Colour Map"

def porta(x, amplitude = 1, lift = 0, frequency = 1, phase = 0):
    y = 0
    x = x * frequency + phase
    x = x % 1.0
    if x < (1/6):
        y = 1
    elif x < (2/6):
        y = 1-(math.cos(math.pi*x*6)+1)/2
    elif x < (3/6):
        y = 0
    elif x < (4/6):
        y = 0
    elif x < (5/6):
        y = 1-(math.cos(math.pi*x*6)+1)/2
    else:
        y = 1
    y = y * amplitude + lift
    return y

def slew():
    pass

def main():
    mpl.style.use("dark_background")
    x = np.linspace(0.0, 1.0, 100)
    y = []
    p = 2

    y_Red = method()
    y_Red.label = "Red"
    y_Red.method = [x, [porta(x, phase = (0/3), amplitude = 0.5, lift = 0.25) for x in x]]
    y_Red.colour = (1.0, 0.0, 0.3)
    y.append(y_Red)

    y_Green = method()
    y_Green.label = "Green"
    y_Green.method = [x, [porta(x, phase = (1/3)) for x in x]]
    y_Green.colour = (0.3, 1.0, 0.0)
    y.append(y_Green)

    y_Blue = method()
    y_Blue.label = "Blue"
    y_Blue.method = [x, [porta(x, phase = (2/3)) for x in x]]
    y_Blue.colour = (0.0, 0.3, 1.0)
    y.append(y_Blue)
    
    plot(x, y)
    mpl.tight_layout(pad = 1.0)
    mpl.show(block = False)

class method:
    def __init__(self):
        pass

def plot(x, y, title = TITLE + " - Plot"):
    figure, axes = mpl.subplots(1, 1, num = title, figsize = (6, 2))
    x_ticks = np.arange(0.0, 1.1, 1 / 6)
    y_ticks = np.arange(0.0, 1.1, 0.5)

    axes.set_title(title)
    axes.set(xlabel = "x", ylabel = "y")
    axes.set(xlim = [0.0, 1.0], ylim = [0.0, 1.0])
    axes.xaxis.set_ticks(x_ticks)
    axes.yaxis.set_ticks(y_ticks)

    labels = []
    for i in range(0, len(y)):
        labels.append(y[i].label)
        thickness = y[i].thickness if hasattr(y[i], "thickness") else 3
        axes.plot(*(y[i].method), color = y[i].colour, linewidth = thickness)
    axes.grid(alpha = 0.5)

if __name__ == "__main__":
    main()
