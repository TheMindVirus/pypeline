import matplotlib.pyplot as mpl
import numpy as np

"""
def midpoints(x_list = []):
    y_list = list(x_list)[:]
    for i in range(0, len(y_list)):
        sl = ()
        for _ in range(y_list[i].ndim):
            y_list[i] = (y_list[i][sl + np.index_exp[:-1]] + y_list[i][sl + np.index_exp[1:]]) / 2.0
            sl += np.index_exp[:]
    return y_list
    
#x = np.linspace(-1.0, 1.0, 11)
#y = np.linspace(-1.0, 1.0, 11)
#z = np.linspace(-1.0, 1.0, 11)

x, y, z = np.indices((17, 17, 17)) / 16.0
ox, oy, oz = midpoints((x, y, z))
equation = (pow(ox - 0.5, 2) + pow(oy - 0.5, 2) + pow(oz - 0.5, 2)) < pow(0.5, 2)
print(equation)
"""

alpha = 0.8

nx = 4
ny = 4
nz = 4

ax = nx + 1
ay = ny + 1
az = nz + 1

sx = ax * 2
sy = ay * 2
sz = az * 2

px = sx + 1
py = sy + 1
pz = sz + 1

aura = [1.0, 0.0, 0.3, alpha]
voxels = np.ndarray((sx, sy, sz), dtype = bool)
ix, iy, iz = np.indices((px, py, pz), dtype = np.float64)

ix = ((ix - ax) / nx)
iy = ((iy - ay) / ny)
iz = ((iz - az) / nz)

for x in range(0, sx):
    for y in range(0, sy):
        for z in range(0, sz):
            voxels[x][y][z] = False

ox = -1
oy = -1
oz = -1

for x in range(0, sx):
    for y in range(0, sy):
        for z in range(0, sz):
            ox1 = ix[x][y][z]
            oy1 = iy[x][y][z]
            oz1 = iz[x][y][z]
            ox2 = ix[x+1][y][z]
            oy2 = iy[x][y+1][z]
            oz2 = iz[x][y][z+1]
            if ox >= ox1 and ox < ox2 \
            and oy >= oy1 and oy < oy2 \
            and oz >= oz1 and oz < oz2:
                voxels[x][y][z] = True

r = 0.8
t = 0.6
default_aura = aura
alternate_aura = [1.0, 1.0, 1.0, alpha]
aura = np.ndarray((sx, sy, sz), dtype = list)
for x in range(0, sx):
    for y in range(0, sy):
        for z in range(0, sz):
            aura[x][y][z] = default_aura
            ox = ix[x][y][z]
            oy = iy[x][y][z]
            oz = iz[x][y][z]
            if ox >= t or ox <= -t \
            or oy >= t or oy <= -t \
            or oz >= t or oz <= -t:
                aura[x][y][z] = alternate_aura

for ox in range(0, sx):
    for oy in range(0, sy):
        for oz in range(0, sz):
            x = ix[ox][oy][oz]
            y = iy[ox][oy][oz]
            z = iz[ox][oy][oz]
            #voxels[ox][oy][oz] = x == y == z
            voxels[ox][oy][oz] = (pow(x, 2) + pow(y, 2) + pow(z, 2)) < pow(r, 2)

dx = 1.0 / (2.0 * nx)
dy = 1.0 / (2.0 * ny)
dz = 1.0 / (2.0 * nz)

vx = ix - dx
vy = iy - dy
vz = iz - dz

equation = filled = voxels

figure = mpl.figure()
axes = figure.add_subplot(projection = "3d")
axes.voxels(vx, vy, vz, equation, facecolors = aura, linewidth = 0)

axes.set_title("sample")
axes.set(xlabel = "x", ylabel = "y", zlabel = "z")
axes.xaxis.set_ticks(np.arange(-1.000001, 1.000001, 0.5))
axes.yaxis.set_ticks(np.arange(-1.000001, 1.000001, 0.5))
axes.zaxis.set_ticks(np.arange(-1.000001, 1.000001, 0.5))
axes.set_xlim((-1.5, 1.5))
axes.set_ylim((-1.5, 1.5))
axes.set_zlim((-1.5, 1.5))
axes.set_aspect("equal")

mpl.show()
