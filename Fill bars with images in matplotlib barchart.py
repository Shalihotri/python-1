import numpy as np
import matplotlib.pyplot as plt

img1 = plt.imread(r'C:\Users\aldal\Desktop\background.jpg')
img2 = plt.imread(r'C:\Users\aldal\Desktop\background2.jpg')
img3 = plt.imread(r'C:\Users\aldal\Desktop\background3.jpg')

data1 = 3
data2 = 4
data3 = 5

images = [img1, img2, img3]
datas = [data1, data2, data3]

def BuildBar(left=0.6):
    for i,j in zip(images, datas):
        width = 0.8
        right = left + width
        height = j
        plt.imshow(i, extent=[left, right, 0, height])
        left = left + 1
    plt.xlim(0, right+0.4)
    plt.ylim(0, height)