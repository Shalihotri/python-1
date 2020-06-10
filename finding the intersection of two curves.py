import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import  LineString

df = pd.read_excel('D:/Coding Practice/data/data_supply-demand.xlsx')

supply = df['Supply']
demand = df['Demand']
price = df['Price(dollar)']

#it's time for visualization
plt.plot(supply,price)
plt.plot(demand,price)

line_1 = LineString(np.column_stack((supply, price)))
line_2 = LineString(np.column_stack((demand, price)))
intersection = line_1.intersection(line_2)

plt.plot(*intersection.xy, 'ro')

plt.show()

x,y = intersection.xy
x,y