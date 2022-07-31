import cv2
import matplotlib.pyplot as plt 
import numpy as np

img = cv2.imread("/home/ericlab/tsuchida/2022_07/annotation/real_data_t_pipe/input/7_14_4_2_48.jpg")
# plt.axis('off')
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# cv2.imshow("win", img)
# cv2.imwrite("/home/ericlab/network/pytorch_yolov3/previous_process/out.jpg", img)
# print(img.shape)
# print(img[12][199])

hist = np.zeros(256)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        hist[img[i][j][0]] += 1
        