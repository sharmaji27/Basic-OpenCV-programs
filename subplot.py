import cv2
import matplotlib.pyplot as plt

path='C:\\Users\\sharma ji\\Pictures\\test\\'

imgpath1= path + '4.2.01.tiff'
imgpath2= path + '4.2.03.tiff'
imgpath3= path + 'lena_color_512.tif'

img1 = cv2.imread(imgpath1)
img2 = cv2.imread(imgpath2)
img3 = cv2.imread(imgpath3)

img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
img3 = cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)

img=[img1,img2,img3]
title=['liquid drop','monkey','lena']

for i in range (3):
    plt.subplot(1,3,i+1)
    plt.title(title[i])
    plt.imshow(img[i])
    plt.xticks([])
    plt.yticks([])
plt.show()