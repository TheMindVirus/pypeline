#pip3 install -U numpy
#pip3 install matplotlib
import math
import numpy as np
import matplotlib.pyplot as mpl

TITLE = "Colour Map"

def porta(x, frequency = 1, phase = 0, amplitude = 1, lift = 0, clamp = 1):
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
    if clamp:
        y = min(max(y, 0.0), 1.0)
    return y

def slew(x, tiers = 3, frequency = 1, phase = 0, amplitude = 1, lift = 0, clamp = 0):
    y = 0
    x = x * frequency + phase
    x = x % 1.0

    if x > 0.5:
        x = 1 - x
    tiers = max(0, tiers)
    if tiers < 2:
        return tiers
    n = 4 * tiers - 2
    steps = tiers - 1
    step = 1 / steps
    tier = 0
    for i in range(1, n):
        k = i / n
        if x <= k:
            if i % 2 == 0:
                y = tier + ((math.cos((math.pi*(x + k)*n))+1)/2) / steps
            else:
                y = tier
            break
        if i % 2 == 0:
            tier += step
        
    y = y * amplitude + lift
    if clamp:
        y = min(max(y, 0.0), 1.0)
    return y

def custom(x, p):
    if p == 1:
        if x <= (1/6):
            return 1
        if x <= (2/6):
            return slew(x, frequency = 3)
        if x <= (4/6):
            return 0
        if x <= (5/6):
            return slew(x, frequency = 3)
        if x <= (6/6):
            return 1
    if p == 2:
        if x <= (1/6):
            return slew(x, frequency = 3)
        if x <= (3/6):
            return 1
        if x <= (4/6):
            return slew(x, frequency = 3)
        if x <= (6/6):
            return 0
    if p == 3:
        if x <= (2/6):
            return 0
        if x <= (3/6):
            return slew(x, frequency = 3)
        if x <= (5/6):
            return 1
        if x <= (6/6):
            return slew(x, frequency = 3)
    return 0

def main():
    mpl.style.use("dark_background")
    x = np.linspace(0.0, 1.0, 100)
    y = []

    y_Red = method()
    y_Red.label = "Red"
    #y_Red.method = [x, [porta(x, phase = (0/3)) for x in x]]
    #y_Red.method = [x, [1 - slew(x, phase = (0/3)) for x in x]]
    y_Red.method = [x, [custom(x, 1) for x in x]]
    y_Red.colour = (1.0, 0.0, 0.3)
    y.append(y_Red)
    
    y_Green = method()
    y_Green.label = "Green"
    #y_Green.method = [x, [porta(x, phase = (1/3)) for x in x]]
    #y_Green.method = [x, [1 - slew(x, phase = (1/3)) for x in x]]
    y_Green.method = [x, [custom(x, 2) for x in x]]
    y_Green.colour = (0.3, 1.0, 0.0)
    y.append(y_Green)

    y_Blue = method()
    y_Blue.label = "Blue"
    #y_Blue.method = [x, [porta(x, phase = (2/3)) for x in x]]
    #y_Blue.method = [x, [1 - slew(x, phase = (2/3)) for x in x]]
    y_Blue.method = [x, [custom(x, 3) for x in x]]
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
