import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath = "C:\\Users\\sharma ji\\Pictures\\test\\cameraman.tif"
img = cv2.imread(imgpath,0)

k = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,k,iterations=2)
dilation = cv2.dilate(img,k,iterations=2)
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,k)
titles = ['original','erosion','dilate','gradient']
img = [img,erosion,dilation,gradient]

for i in range (4):
    plt.subplot(2,2,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.title(titles[i])
    plt.imshow(img[i],cmap='gray')
plt.show()
