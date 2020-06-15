import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2)
fig.patch.set_facecolor('oldlace')

x1 = np.linspace(0,8)
x2 = np.linspace(0,3)

y1 = np.sin(np.pi*x1)
y2 = np.cos(x2*np.pi*3)

axs[0].plot(x1,y1,'o-')
axs[0].set_title('sin (x1*\u03c0)')
axs[0].set_facecolor('snow')
axs[0].grid(True)

axs[1].plot(x2,y2,'o-')
axs[1].set_title('cos (3*x2*\u03c0)')
axs[1].set_facecolor('snow')
axs[1].grid(True)

plt.tight_layout()