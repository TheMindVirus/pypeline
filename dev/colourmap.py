#pip3 install -U numpy
#pip3 install matplotlib
import math
import numpy as np
import matplotlib.pyplot as mpl

TITLE = "Colour Map"
    
def main():
    mpl.style.use("dark_background")
    x = np.linspace(0.0, 1.0, 100)
    y = []
    p = 2 #11 #5 #np.pi / 2 #5 # 2

    y_Red = method()
    y_Red.label = "Red"
    #y_Red.method = [x, [min(max(2 - abs(6*x) if x < 0.5 else 2 - abs(6*(x-1)), 0.0), 1.0) for x in x]]
    #y_Red.method = [x, [(math.sin(math.tau*(x))+1)/2 for x in x]]
    #y_Red.method = [x, [(math.cos(math.tau * ((1.5 * x))) + 1) / 2 if x < (1/3) else (math.cos(math.tau * ((1.5 * x) - 0.5)) + 1) / 2 if x > (2/3) else 0 for x in x]]
    #y_Red.method = [x, [np.sqrt(max(0.0, 1.0 - pow(3 * x, 2))) if x < 0.5 else np.sqrt(max(0.0, 1.0 - pow(3 * (1.0 - x), 2))) for x in x]]
    #y_Red.method = [x, [pow(3 * ((1/3) - x), 2) if x < (1/3) else 0 if x < (2/3) else pow(3 * (x - (2/3)), 2) for x in x]]
    #y_Red.method = [x, [1.0 - pow(3 * x, p) if x < (1/3) else 0 if x < (2/3) else 1.0 - pow(3 * (x - 1), p) for x in x]]
    #y_Red.method = [x, [1.0 - pow(3 * x, p) if x < (1/3) else 0 if x < (2/3) else 1.0 - pow(3 * (1 - x), p) for x in x]]
    #y_Red.method = [x, [1 if x < (1/6) else 1.0 - pow(6 * (x - (1/6)), p) if x < (2/6) else 0 if x < (3/6) else 0 if x < (4/6) else 1.0 - pow(6 * ((5/6) - x), p) if x < (5/6) else 1 for x in x]]
    #y_Red.method = [x, [1 if x < (1/6) else (math.cos(math.tau * (3 * (x + (1/6)))) + 1) / 2 if x < (2/6) else 0 if x < (4/6) else (math.cos(math.tau * (3 * (x - (1/6)))) + 1) / 2 if x < (5/6) else 1 for x in x]]
    #y_Red.method = [x, [1 if x < (1/6) else np.sqrt(pow((3 * (1.0 - x)), 2)) if x < (2/6) else 0 if x < (4/6) else (math.cos(math.tau * (3 * (x - (1/6)))) + 1) / 2 if x < (5/6) else 1 for x in x]]
    y_Red.method = [x, [1 if x < (1/6) else (np.sqrt(max(0.0, 1.0 - pow(12 * (x - (1/6)), p))) + 1) / 2 if x < (1.5/6) else (1.0 - np.sqrt(max(0.0, 1.0 - pow(12 * ((2/6) - x), p)))) / 2 if x < (2/6) else 0 if x < (4/6) else (1.0 - np.sqrt(max(0.0, 1.0 - pow(12 * (x - (4/6)), p)))) / 2 if x < (4.5/6) else (np.sqrt(max(0.0, 1.0 - pow(12 * ((5/6) - x), p))) + 1) / 2 if x < (5/6) else 1 for x in x]]
    #y_Red.colour = (1.0, 0.0, 0.0)
    y_Red.colour = (1.0, 0.0, 0.3)
    y.append(y_Red)

    y_Green = method()
    y_Green.label = "Green"
    #y_Green.method = [x, [min(max(2 - abs(6*(x - (1/3))), 0.0), 1.0) for x in x]]
    #y_Green.method = [x, [(math.cos(math.tau * ((1.5 * x) + (1/3))) + 1) / 2 for x in x]]
    #y_Green.method = [x, [np.sqrt(max(0.0, 1.0 - pow(3 * (x - (1/3)), 2))) for x in x]]
    #y_Green.method = [x, [pow(3 * x, 2) if x < (1/3) else pow(3 * (x - (2/3)), 2) if x < (2/3) else 0 for x in x]]
    #y_Green.method = [x, [1.0 - pow(3 * (x - (1/3)), p) if x < (1/3) else 1.0 - pow(3 * (x - (1/3)), p) if x < (2/3) else 0 for x in x]]
    #y_Green.method = [x, [1.0 - pow(3 * ((1/3) - x), p) if x < (1/3) else 1.0 - pow(3 * (x - (1/3)), p) if x < (2/3) else 0 for x in x]]
    #y_Green.method = [x, [1.0 - pow(6 * ((1/6) - x), p) if x < (1/6) else 1 if x < (2/6) else 1 if x < (3/6) else 1.0 - pow(6 * (x - (3/6)), p) if x < (4/6) else 0 if x < (5/6) else 0 for x in x]]
    #y_Green.method = [x, [(math.cos(math.tau * (3 * (x + (1/6)))) + 1) / 2 if x < (1/6) else 1 if x < (3/6) else (math.cos(math.tau * (3 * (x + (1/6)))) + 1) / 2 if x < (4/6) else 0 for x in x]]
    y_Green.method = [x, [(1.0 - np.sqrt(max(0.0, 1.0 - pow(12 * (x - (0/6)), p)))) / 2 if x < (0.5/6) else (np.sqrt(max(0.0, 1.0 - pow(12 * ((1/6) - x), p))) + 1) / 2 if x < (1/6) else 1 if x < (3/6) else (np.sqrt(max(0.0, 1.0 - pow(12 * (x - (3/6)), p))) + 1) / 2 if x < (3.5/6) else (1.0 - np.sqrt(max(0.0, 1.0 - pow(12 * ((4/6) - x), p)))) / 2 if x < (4/6) else 0 for x in x]]
    #y_Green.colour = (0.0, 1.0, 0.0)
    y_Green.colour = (0.3, 1.0, 0.0)
    y.append(y_Green)

    y_Blue = method()
    y_Blue.label = "Blue"
    #y_Blue.method = [x, [min(max(2 - abs(6*(x - (2/3))), 0.0), 1.0) for x in x]]
    #y_Blue.method = [x, [(math.cos(math.tau * ((1.5 * x) + (2/3))) + 1) / 2 for x in x]]
    #y_Blue.method = [x, [np.sqrt(max(0.0, 1.0 - pow(3 * (x - (2/3)), 2))) for x in x]]
    #y_Blue.method = [x, [0 if x < (1/3) else pow(3 * (x - (1/3)), 2) if x < (2/3) else pow(3 * (x - 1), 2) for x in x]]
    #y_Blue.method = [x, [0 if x < (1/3) else 1.0 - pow(3 * (x - (2/3)), p) if x < (2/3) else 1.0 - pow(3 * (x - (2/3)), p) for x in x]]
    #y_Blue.method = [x, [0 if x < (1/3) else 1.0 - pow(3 * ((2/3) - x), p) if x < (2/3) else 1.0 - pow(3 * (x - (2/3)), p) for x in x]]
    #y_Blue.method = [x, [0 if x < (1/6) else 0 if x < (2/6) else 1.0 - pow(6 * ((3/6) - x), p) if x < (3/6) else 1 if x < (4/6) else 1 if x < (5/6) else 1.0 - pow(6 * (x - (5/6)), p) for x in x]]
    #y_Blue.method = [x, [(0 if x < (2/6) else (math.cos(math.tau * (3 * (x + (1/6))))) + 1) / 2 if x < (3/6) else 1 if x < (5/6) else (math.cos(math.tau * (3 * (x + (1/6)))) + 1) / 2 for x in x]]
    y_Blue.method = [x, [0 if x < (2/6) else (1.0 - np.sqrt(max(0.0, 1.0 - pow(12 * (x - (2/6)), p)))) / 2 if x < (2.5/6) else (np.sqrt(max(0.0, 1.0 - pow(12 * ((3/6) - x), p))) + 1) / 2 if x < (3/6) else 1 if x < (5/6) else (np.sqrt(max(0.0, 1.0 - pow(12 * (x - (5/6)), p))) + 1) / 2 if x < (5.5/6) else (1.0 - np.sqrt(max(0.0, 1.0 - pow(12 * ((6/6) - x), p)))) / 2 for x in x]]
    #y_Blue.colour = (0.0, 0.0, 1.0)
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
    #axes.axis("square")
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
