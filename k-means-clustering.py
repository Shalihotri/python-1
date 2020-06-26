#necessary package
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#data source
df= pd.read_excel('D:/Coding Practice/data/data_kmeans.xlsx')

#amount_of_cluster
amount_of_cluster=4

#initial centroid
centroid_x = [1,3,5,7]
centroid_y = [1,3,5,7]

#empty list that will be filled later
in_cluster_1x = []
in_cluster_1y = []
in_cluster_2x = []
in_cluster_2y = []
in_cluster_3x = []
in_cluster_3y = []
in_cluster_4x = []
in_cluster_4y = []

#columns from data source
x = np.array(df['Love Spicy Chicken'])
y = np.array(df['Love Crispy Chicken'])

#the main process
for j in np.arange(100):
    range_to_centroid = []
    for k in np.arange(amount_of_cluster):
        range_to_centroid.append(np.sqrt((x-centroid_x[k])**2 + (y-centroid_y[k])**2))
    range_to_centroid = np.array([range_to_centroid]).transpose()
    for i in np.arange(len(df.index)):
        if min(range_to_centroid[i]) == range_to_centroid[i,0]:
            in_cluster_1x.append(x[i])
            in_cluster_1y.append(y[i])
        elif min(range_to_centroid[i]) == range_to_centroid[i,1]:
            in_cluster_2x.append(x[i])
            in_cluster_2y.append(y[i])
        elif min(range_to_centroid[i]) == range_to_centroid[i,2]:
            in_cluster_3x.append(x[i])
            in_cluster_3y.append(y[i])
        elif min(range_to_centroid[i]) == range_to_centroid[i,3]:
            in_cluster_4x.append(x[i])
            in_cluster_4y.append(y[i])
        else:
            pass

    centroid_x = []
    centroid_y = []


    centroid_x.append(np.mean(in_cluster_1x))
    centroid_y.append(np.mean(in_cluster_1y))
    centroid_x.append(np.mean(in_cluster_2x))
    centroid_y.append(np.mean(in_cluster_2y))
    centroid_x.append(np.mean(in_cluster_3x))
    centroid_y.append(np.mean(in_cluster_3y))
    centroid_x.append(np.mean(in_cluster_4x))
    centroid_y.append(np.mean(in_cluster_4y))

    n_in_cluster1 = len(in_cluster_1x)
    n_in_cluster2 = len(in_cluster_2x)
    n_in_cluster3 = len(in_cluster_3x)
    n_in_cluster4 = len(in_cluster_4x)

    in_cluster_1x = []
    in_cluster_1y = []
    in_cluster_2x = []
    in_cluster_2y = []
    in_cluster_3x = []
    in_cluster_3y = []
    in_cluster_4x = []
    in_cluster_4y = []

#after 100 iteration, here's the scatterplot of all data point and the centroids
#data have blue color and centroid have orange color

plt.scatter(df['Love Spicy Chicken'], df['Love Crispy Chicken'])
df_result = pd.DataFrame(
    np.array([
        [centroid_x[0], centroid_y[0]],
        [centroid_x[1], centroid_y[1]],
        [centroid_x[2], centroid_y[2]],
        [centroid_x[3], centroid_y[3]],
    ]), columns=['Love Spicy Chicken','Love Crispy Chicken']
)
plt.scatter(df_result['Love Spicy Chicken'], df_result['Love Crispy Chicken'])
plt.xlabel('Love Spicy Chicken')
plt.ylabel('Love Crispy Chicken')
plt.title('4-means clustering', size=20, pad=20)

#here's the final table
df_result['Number of People'] = [n_in_cluster1, n_in_cluster2, n_in_cluster3, n_in_cluster4]