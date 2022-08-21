
import cv2

image_path = "/home/ericlab/tsuchida/2022_07/annotation/real_data_t_pipe_ano_again/images/7_14_4_2_48.jpg"
img = cv2.imread(image_path)
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])

img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
output = "/home/ericlab/network/pytorch_yolov3/previous_process/res1.png"
# cv2.imshow('CLAHE', output)
# cv2.waitKey(0)
cv2.imwrite(output, img)
