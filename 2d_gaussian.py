import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker, cm

A = 1
size = 50
sigma_x = 4
sigma_y = 2


x = np.linspace(-9, 9, size)
y = np.linspace(-9, 9, size)

x, y = np.meshgrid(x, y)
z = (A/(2*np.pi*sigma_x*sigma_y) * np.exp(-(x**2/(2*sigma_x**2)
     + y**2/(2*sigma_y**2))))

# Automatic selection of levels works; setting the
# log locator tells contourf to use a log scale:
fig, ax = plt.subplots()
cs = ax.contourf(x, y, z, cmap=cm.gist_gray)

# Alternatively, you can manually set the levels
# and the norm:
# lev_exp = np.arange(np.floor(np.log10(z.min())-1),
#                    np.ceil(np.log10(z.max())+1))
# levs = np.power(10, lev_exp)
# cs = ax.contourf(X, Y, z, levs, norm=colors.LogNorm())

cbar = fig.colorbar(cs)

plt.show()
