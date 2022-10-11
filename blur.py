import cv2
import matplotlib.pyplot as plt

imgpath = "C:\\Users\\sharma ji\\Pictures\\test\\lena_color_512.tif"
img1 = cv2.imread(imgpath)
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

box = cv2.boxFilter(img1,-1,(25,25))
blur = cv2.blur(img1,(15,15))
gaussian = cv2.GaussianBlur(img1,(17,17),0)

img=[img1,box,blur,gaussian]
title = ['original','box','blur','gaussian']

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.title(title[i])
    plt.imshow(img[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()