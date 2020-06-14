import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

x=np.arange(1,100,2)

#f(x)
y=x**2 + x - 2

#visualization
sns.lineplot(x=x, y=y)
ax.grid(True)
ax.text(0.05, 0.83, 'y = x$^2$ + x - 2', fontsize=22, transform=ax.transAxes,
bbox={'facecolor':'white', 'edgecolor':'red', 'alpha':1, 'boxstyle':'round'})