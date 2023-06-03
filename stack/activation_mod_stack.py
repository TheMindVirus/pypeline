#pip3 install -U numpy
#pip3 install matplotlib
import numpy as np
import matplotlib.pyplot as mpl

TITLE = "Activation Methods"
    
def main():
    title = "Activation Methods"
    mpl.style.use("dark_background")
    x = np.linspace(-10.0, 10.0, 100)
    y = []

    y_Redline = method()
    y_Redline.title = "Redline"
    y_Redline.method = [x, ((x % 2) > 1) + 1]
    y_Redline.x_range = [-10.0, 10.1, 1.0]
    y_Redline.y_range = [-0.0, 2.1, 1.0]
    y_Redline.colour = [1.0, 0.0, 0.2]
    y_Redline.thickness = 5
    y_Redline.x_label = "Time(ps)"
    y_Redline.y_label = "Voltage(V)"
    y.append(y_Redline)

    y_PAM3 = method()
    y_PAM3.title = "PAM3"
    y_PAM3.method = [x, [(round(x - 0.5) % 3) - 1 if (x % 6) < 3 else (round(-x - 0.5) % 3) - 1 for x in x]]
    y_PAM3.x_range = [-10.0, 10.1, 1.0]
    y_PAM3.y_range = [-1.0, 1.1, 1.0]
    y_PAM3.colour = [0.0, 1.0, 0.2]
    y_PAM3.thickness = 5
    y_PAM3.x_label = "Time(X)"
    y_PAM3.y_label = "Level(Y)"
    y.append(y_PAM3)

    y_PAM5 = method()
    y_PAM5.title = "PAM5"
    y_PAM5.method = [x, [(round(x - 0.5) % 5) - 2 if (x % 10) < 5 else (round(-x - 0.5) % 5) - 2 for x in x]]
    y_PAM5.x_range = [-10.0, 10.1, 1.0]
    y_PAM5.y_range = [-2.0, 2.1, 1.0]
    y_PAM5.colour = [0.0, 1.0, 1.0]
    y_PAM5.thickness = 5
    y_PAM5.x_label = "Time(X)"
    y_PAM5.y_label = "Level(Y)"
    y.append(y_PAM5)

    stack(x, y, len(y), 1)
    
    mpl.tight_layout(pad = 1.0)
    mpl.show(block = False)

class method:
    def __init__(self):
        pass

def stack(x, y, rows, cols, title = TITLE + " - Stack"):
    figure, axes = mpl.subplots(rows, cols, num = title)

    for i in range(0, len(y)):
        axes[i].set_title(y[i].title)
        axes[i].set(xlabel = y[i].x_label, ylabel = y[i].y_label)
        axes[i].set(xlim = y[i].x_range[0:2], ylim = y[i].y_range[0:2])
        axes[i].xaxis.set_ticks(np.arange(*(y[i].x_range)))
        axes[i].set_xticklabels(axes[i].get_xticks(), rotation = 90)
        axes[i].yaxis.set_ticks(np.arange(*(y[i].y_range)))
        axes[i].plot(*(y[i].method), color = y[i].colour)
        axes[i].grid(alpha = 0.5)

if __name__ == "__main__":
    main()
