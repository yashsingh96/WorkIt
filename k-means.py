import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from sys import argv
import argparse

img = cv2.imread(argv[1])
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure()
plt.axis("off")
#plt.imshow(img),plt.colorbar(),plt.show()

clusters = 10
image = img.reshape((img.shape[0] * img.shape[1], 3))
clt = KMeans(n_clusters = clusters)
clt.fit(image)

print(image)
print(clt.cluster_centers_)
print(clt.labels_)

classification = clt.labels_.reshape(img.shape[:2])
#getting shirt color

x_range = list(range(int(img.shape[1]*0.4), int(img.shape[1]*0.6)))
y_top = list(range(int(img.shape[0]*0.5)))
y_bottom = list(range(int(img.shape[0]*0.5), int(img.shape[0])))

print(img.shape)

print(classification.shape)
shirt_count = np.bincount(classification[:int(img.shape[0]*0.6), int(img.shape[1]*0.33):int(img.shape[1]*0.66)].flatten())
pants_count = np.bincount(classification[int(img.shape[0]*0.7):,int(img.shape[1]*0.33):int(img.shape[1]*0.66)].flatten())

bar = np.zeros((50, 100, 3), dtype='uint8')

shirt_color = clt.cluster_centers_[np.argmax(shirt_count)]
pants_color = clt.cluster_centers_[np.argmax(pants_count)]

print(shirt_color)
print(pants_color)

bar[:,:50] = shirt_color
bar[:,50:] = pants_color

plt.imshow(bar),plt.colorbar(),plt.show()
