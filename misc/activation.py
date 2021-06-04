#pip3 install -U numpy
#pip3 install matplotlib
import numpy as np
import matplotlib.pyplot as mpl

TITLE = "Activation Methods"
    
def main():
    title = "Activation Methods"
    mpl.style.use("dark_background")
    
    x = np.linspace(-1.0, 1.0, 100)
    y = []

    y_Sigmoid = method()
    y_Sigmoid.label = "Sigmoid"
    y_Sigmoid.method = [x, ((1.0 / (1.0 + np.exp(-6.0 * x))) * 2.0) - 1.0]
    y_Sigmoid.colour = (0.0, 1.0, 1.0)
    y.append(y_Sigmoid)

    y_ReLU = method()
    y_ReLU.label = "ReLU"
    y_ReLU.method = [x, [max(0, i) for i in x]]
    y_ReLU.colour = (1.0, 0.0, 0.0)
    y_ReLU.thickness = 5
    y.append(y_ReLU)

    y_SoftMax = method()
    y_SoftMax.label = "SoftMax"
    y_SoftMax.method = [x, (np.exp(x * 10.0) * 5.0) / (np.sum(np.exp(x * 10.0)))] #???
    y_SoftMax.colour = (1.0, 1.0, 0.0)
    y.append(y_SoftMax)

    y_Sinusoidal = method()
    y_Sinusoidal.label = "Sinusoidal"
    y_Sinusoidal.method = [x, np.sin(0.5 * np.pi * x)]
    y_Sinusoidal.colour = (1.0, 0.7, 0.0)
    y.append(y_Sinusoidal)

    y_Linear = method()
    y_Linear.label = "Linear"
    y_Linear.method = [x, x]
    y_Linear.colour = (0.0, 1.0, 0.0)
    y.append(y_Linear)

    y_Circular = method()
    y_Circular.label = "Circular"
    y_Circular.method = [x, [-1.0 * np.sqrt(1.0 - pow(i, 2)) + 1.0 if i > 0.0 else (np.sqrt(1.0 - pow(i, 2))) - 1.0 for i in x]]
    #y_Circular.method = [x, [(np.sqrt(1.0 - pow((i - 1.0) * 2.0, 2)) + 1.0) * 0.5 if i > 0.5 else (-1.0 * np.sqrt(1.0 - pow(i * 2.0, 2))) * 0.5 + 0.5 if i > 0.0 else 0.0 for i in x]]
    #y_Circular.method = [x, [1.0 if i > 1.0 else (-1.0 * np.sqrt(1.0 - pow((i - 0.5) * 2.0, 2)) + 1.0) * 0.5 + 0.5 if i >= 0.5 else (np.sqrt(1.0 - pow((i - 0.5) * 2.0, 2)) + 1.0) * 0.5 - 0.5 if i > 0.0 else 0.0 for i in x]]
    #y_Circular.method = [x, [np.sqrt(1.0 - pow((i - 1.0), 2)) if i > 0.0 else 0.0 for i in x]]
    y_Circular.colour = (0.7, 0.0, 1.0)
    y_Circular.thickness = 7
    y.append(y_Circular)

    y_Square = method()
    y_Square.label = "Square"
    y_Square.method = [x, [1.0 if i >= 0.0 else -1.0 for i in x]]
    y_Square.colour = (0.0, 0.0, 1.0)
    y.append(y_Square)

    y_Butterfly = method()
    y_Butterfly.label = "Butterfly"
    y_Butterfly.method = [x, abs(x)]
    y_Butterfly.colour = (1.0, 0.7, 1.0)
    y.append(y_Butterfly)

    y_Hyperbolic = method()
    y_Hyperbolic.label = "Hyperbolic"
    y_Hyperbolic.method = [x, pow(x, 2)]
    y_Hyperbolic.colour = (1.0, 0.35, 0.7)
    y.append(y_Hyperbolic)

    scope(x, y)
    subplot(x, y, 3, 3)
    
    mpl.tight_layout(pad = 1.0)
    mpl.show(block = False)

class method:
    def __init__(self):
        pass

def scope(x, y, title = TITLE + " - Scope"):
    figure, axes = mpl.subplots(1, 1, num = title)
    ticks = np.arange(min(x), max(x) + 0.5, 0.5)

    axes.set_title(title)
    axes.axis("square")
    axes.set(xlabel = "x", ylabel = "y")
    axes.set(xlim = [-1.1, 1.1], ylim = [-1.1, 1.1])
    axes.xaxis.set_ticks(ticks)
    axes.yaxis.set_ticks(ticks)

    labels = []
    for i in range(0, len(y)):
        labels.append(y[i].label)
        thickness = y[i].thickness if hasattr(y[i], "thickness") else 1
        axes.plot(*(y[i].method), color = y[i].colour, linewidth = thickness)

    axes.grid(alpha = 0.5)

def subplot(x, y, rows, cols, title = TITLE + " - Subplot"):
    figure, axes = mpl.subplots(rows, cols, num = title)
    ticks = np.arange(min(x), max(x) + 0.5, 0.5)

    for i in range(0, len(y)):
        col = int(i % cols)
        row = int((i - col) / cols)
        axes[row][col].set_title(y[i].label)
        axes[row][col].axis("square")
        axes[row][col].set(xlabel = "x", ylabel = "y")
        axes[row][col].set(xlim = [-1.1, 1.1], ylim = [-1.1, 1.1])
        axes[row][col].xaxis.set_ticks(ticks)
        axes[row][col].set_xticklabels(axes[row][col].get_xticks(), rotation = 90)
        axes[row][col].yaxis.set_ticks(ticks)
        axes[row][col].plot(*(y[i].method), color = y[i].colour)
        axes[row][col].grid(alpha = 0.5)

if __name__ == "__main__":
    main()
