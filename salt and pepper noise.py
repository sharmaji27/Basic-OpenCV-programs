import cv2
import random
import numpy as np

imgpath = "C:\\Users\\sharma ji\\Pictures\\test\\lena_color_512.tif"
img = cv2.imread(imgpath)

rows,cols,channels = img.shape
output = np.zeros(img.shape,np.uint8)
p=0.05

for i in range(rows):
    for j in range (cols):
        r=random.random()
        if r < p/2:
            #pepper noise
            output[i][j] = [0,0,0]
        elif r <p:
            # salt noise
            output[i][j] = [255,255,255]
        else:
            output[i][j] = img[i][j]
cv2.imshow('noised image ',output)
cv2.waitKey(0)
cv2.destroyAllWindows()