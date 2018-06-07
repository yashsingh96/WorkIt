from sys import argv

import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


def prune(labels, lst, threshold):
    for index in range(len(lst) - 1):
        for i in range(index + 1, len(lst)):
            if lst[index][0] > 0 and lst[i][0] > 0 and abs(lst[index][0] - lst[i][0]) < threshold and abs(
                    lst[index][1] - lst[i][1]) < threshold and abs(lst[index][2] - lst[i][2]) < threshold:
                lst[i] = (-1, -1, index)
    for i in range(len(lst)):
        if lst[i][0] < 0:
            labels[labels == i] = lst[i][2]
    idx = 0
    # print(lst)

    while idx < len(lst):
        if lst[idx][0] < 0:
            lst = np.delete(lst, idx, axis=0)
            for i in range(idx, len(lst)):
                labels[labels == i + 1] = i
        else:
            idx += 1
    # print(labels[labels >= len(lst)])
    # print(lst)
    return lst, labels


def get_colours(image):
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.figure()
    plt.axis("off")
    # plt.imshow(img),plt.colorbar(),plt.show()

    clusters = 8
    image = img.reshape((img.shape[0] * img.shape[1], 3))
    clt = KMeans(n_clusters=clusters)
    clt.fit(image)

    labels = np.copy(clt.labels_)
    centers = np.copy(clt.cluster_centers_)

    centers, labels = prune(labels, centers, 40)

    clusters = len(centers)

    classification = labels.reshape(img.shape[:2])
    # getting shirt color

    x_range = list(range(int(img.shape[1] * 0.4), int(img.shape[1] * 0.6)))
    y_top = list(range(int(img.shape[0] * 0.5)))
    y_bottom = list(range(int(img.shape[0] * 0.5), int(img.shape[0])))

    top_count = np.bincount(
        classification[:int(img.shape[0] * 0.5), int(img.shape[1] * 0.25):int(img.shape[1] * 0.75)].flatten())
    bottom_count = np.bincount(
        classification[int(img.shape[0] * 0.5):, int(img.shape[1] * 0.25):int(img.shape[1] * 0.75)].flatten())

    # find background color
    back_x = [0, 1, img.shape[1] - 2, img.shape[1] - 1]
    back_y = [0, 1, img.shape[0] - 2, img.shape[0] - 1]
    count_back = [0 for x in range(clusters)]
    for i in back_x:
        for j in back_y:
            count_back[classification[j, i]] += 1

    background_color = np.argmax(count_back)
    top_count[background_color] = 0
    bottom_count[background_color] = 0

    bar = np.zeros((100, 200, 3), dtype='uint8')

    total_top = np.sum(top_count)
    total_bottom = np.sum(bottom_count)
    top_curr = 0
    bot_curr = 0

    top_rank = []
    bottom_rank = []

    for i in range(clusters - 1):
        max_top = np.argmax(top_count)
        max_bot = np.argmax(bottom_count)
        top_next = top_curr + int(top_count[max_top] / total_top * 100)
        bot_next = bot_curr + int(bottom_count[max_bot] / total_bottom * 100)
        top_rank.append((centers[max_top], int(top_count[max_top] / total_top * 100)))
        bottom_rank.append((centers[max_bot], int(bottom_count[max_bot] / total_bottom * 100)))

        if top_next < 100 and bot_next < 100:
            bar[top_curr:top_next, :100] = centers[max_top]
            bar[bot_curr:bot_next, 100:] = centers[max_bot]

        top_curr = top_next
        bot_curr = bot_next
        top_count[max_top] = 0
        bottom_count[max_bot] = 0

    plt.imshow(bar), plt.colorbar(), plt.show()
    return top_rank, bottom_rank
    # print(top_rank)
    # print(bottom_rank)

