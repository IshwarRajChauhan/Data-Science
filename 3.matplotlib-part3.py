import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 11)
y = x**2

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, y, color='blue', linewidth=2, alpha=0.5, linestyle='-',
        marker='o',markersize=10,markerfacecolor='green', markeredgewidth=3)
ax.set_xlim([0,3])
ax.set_ylim([0,2])
plt.show()





















