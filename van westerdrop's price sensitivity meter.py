#necessary package
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import LineString

#dataset
df = pd.read_excel('D:/Coding Practice/data/data_van_westerdorp.xlsx')

#some tweaks to the dataset
df['CDF'] = (np.arange(1, len(df.index)+1,1)/len(df.index)).round(3)
df['1-CDF'] = 1 - df['CDF']

#----VISUALIZATION----
#Basic Visualization
plt.plot(df['too expensive'], df['CDF'])
plt.plot(df['expensive'], df['CDF'])
plt.plot(df['cheap'], df['1-CDF'])
plt.plot(df['too cheap'], df['1-CDF'])

#Label, Title, Legend
plt.legend(['too expensive','expensive','cheap','too cheap'], bbox_to_anchor=(1,1))
plt.title("Van Westerdorp's Price Sensitivity Meter", pad=20, size=18)
plt.xlabel('Price (USD)')
plt.ylabel('CDF')

#Annotation
plt.annotate('PMC', xy=(11000,0.3))
plt.annotate('IP', xy=(23000,0.42))
plt.annotate('PME', xy=(30000,0.32))
plt.annotate('OPP', xy=(18000,0.07))
plt.grid(True)

#Mark intersection point with red dots
too_expensive = LineString(np.column_stack((df['too expensive'],df['CDF'])))
expensive = LineString(np.column_stack((df['expensive'], df['CDF'])))
cheap = LineString(np.column_stack((df['cheap'], df['1-CDF'])))
too_cheap = LineString(np.column_stack((df['too cheap'], df['1-CDF'])))

intersection_1 = expensive.intersection(cheap)
intersection_2 = too_expensive.intersection(cheap)
intersection_3 = expensive.intersection(too_cheap)
intersection_4 = too_expensive.intersection(too_cheap)

plt.plot(*intersection_1.xy, 'ro')
plt.plot(*intersection_2.xy, 'ro')
plt.plot(*intersection_3.xy, 'ro')
plt.plot(*intersection_4.xy, 'ro')

plt.show()

#Finding intersection point x-coordinates (price in USD)
IP = round(intersection_1.x)
PME = round(intersection_2.x)
PMC = round(intersection_3.x)
OPP = round(intersection_4.x)

print(('IP is ' + str(f'{IP:,}')))
print(('PME is ' + str(f'{PME:,}')))
print(('PMC is ' + str(f'{PMC:,}')))
print(('OPP is ' + str(f'{OPP:,}')))