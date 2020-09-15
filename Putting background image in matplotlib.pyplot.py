import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

name_of_fruit = ['banana','apple','orange']
name_of_fruit_code = np.array([1,2,3])
amount_sold = [2,2,3]

ax.bar(name_of_fruit_code, amount_sold, color=['yellow','red','orange'],
edgecolor='black',linewidth=3,alpha=0.8)

ax.hlines(amount_sold, 0, name_of_fruit_code+0.4, linestyles='dotted', color='white')

background = plt.imread(r'C:\Users\aldal\Desktop\background2.jpg')
ax.imshow(background, extent=[0,4,0,3.5])

plt.xticks(name_of_fruit_code, name_of_fruit)
plt.yticks(np.arange(1,4))
plt.xlabel('Name of Fruit')
plt.ylabel('Amount of Fruit(s) Sold')