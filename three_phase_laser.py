import matplotlib.pyplot as mpl
import matplotlib.animation as ani
import matplotlib.patheffects as pfx
import numpy as np
import math as math

title = num = "Three Phase LASER"

mpl.style.use("dark_background")
ani.Animation = ani.FuncAnimation
figure, axes = mpl.subplots(num = title)

tau = 2.0 * math.pi
third = tau / 3.0
phase1 = third * 1
phase2 = third * 2
phase3 = third * 3

x = np.arange(0.0, 2.0 * math.pi, 0.01)
x_ticks = np.arange(0.0, 1.1, 0.1)
y_ticks = np.arange(-1.0, 1.1, 0.25)
y1 = axes.plot(x, np.sin(x), color = "#FF0066", linewidth = 1)[0]
y2 = axes.plot(x, np.sin(x), color = "#FF0066", linewidth = 2)[0]
y3 = axes.plot(x, np.sin(x), color = "#FF0066", linewidth = 3)[0]

axes.set_title(title, color = "#FF0066", size = "30")
axes.set_xlabel("x (au)", color = "#7F7FFF")
axes.set_ylabel("y (au)", color = "#7F7FFF")
axes.set(xlim = [0.0, 1.0], ylim = [0.0, 1.0])
axes.xaxis.set_ticks(x_ticks)
axes.yaxis.set_ticks(y_ticks)
axes.xaxis.set_tick_params(labelcolor = "#FF0066")
axes.yaxis.set_tick_params(labelcolor = "#FF0066")

class dilation(pfx.AbstractPathEffect):
    #def draw_path(self, *args, **kwargs):
    #    custom(mode = "pre").draw_path(*args, **kwargs)
    #    retval = super().draw_path(*args, **kwargs)
    #    custom(mode = "post").draw_path(*args, **kwargs)
    #    return retval
    def draw_path(self, renderer, gc, tpath, tmod, tface = None):
        #if isinstance(renderer, pfx.PathEffectRenderer):
        #    renderer = renderer._renderer
        #mod = tmod
        #mod = tmod.__class__(tmod)
        #print(dir(tmod))
        #print(type(tmod.scale))
        #mod.scale(0.5)
        #renderer.draw_path(gc, tpath, mod, tface)
        #mod.scale(2.0)
        scale = 1.01
        nscale = 1 / scale
        tmod.scale(scale);
        renderer.draw_path(gc, tpath, tmod, tface)
        tmod.scale(nscale)
        renderer.draw_path(gc, tpath, tmod, tface)
        tmod.scale(nscale)
        renderer.draw_path(gc, tpath, tmod, tface)
        tmod.scale(scale)
        tface = [0.0, 0.0, 0.1, 0.5]
        return renderer.draw_path(gc, tpath, tmod, tface)

def loop(i):
    anim_stack = []
    velocity = i / 100
    y1.set_ydata(np.sin((x * tau) + phase1 + velocity))
    y2.set_ydata(np.sin((x * tau) + phase2 + velocity))
    y3.set_ydata(np.sin((x * tau) + phase3 + velocity))
    #y1.set_path_effects([pfx.withSimplePatchShadow(offset = (0, 0), shadow_rgbFace = "#FFFFFF", rho = 0.1, alpha = None)])
    y1.set_path_effects([dilation()])
    y2.set_path_effects([dilation()])
    y3.set_path_effects([dilation()])
    anim_stack.append(y1)
    anim_stack.append(y2)
    anim_stack.append(y3)
    return anim_stack

anim = ani.Animation(figure, loop, interval = 10,
                     blit = True, save_count = 50)
mpl.show()
