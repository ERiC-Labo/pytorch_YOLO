import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import time

# input_dir = "/home/ericlab/tsuchida/2022_07/annotation/real_data_t_pipe/images"
# output_dir = "/home/ericlab/tsuchida/2022_07/annotation/real_hist_data_t_pipe/images"

# files = os.listdir(input_dir)

# for file in files:
#     img = cv2.imread(os.path.join(input_dir, file), 0)
#     equ = cv2.equalizeHist(img)
#     cv2.imwrite(os.path.join(output_dir, file), equ)


img = cv2.imread("/media/ericlab/56A6-0775/image/image/sensor_1.png",0)
start = time.time()
equ = cv2.equalizeHist(img)
end = time.time()
print(end - start)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('/media/ericlab/56A6-0775/image/image/sensor_1_kai.png',equ)