import cv2
import matplotlib.pyplot as plt

path='C:\\Users\\sharma ji\\Pictures\\test\\'

imgpath1 = path + '4.2.06.tiff'


img1 = cv2.imread(imgpath1)
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

img2 = cv2.imread(imgpath1,0)

img3=abs(255-img1)
img4=abs(255-img2)

img = [img1,img2,img3,img4]
title = ['coloured','gray','coloured-negative','gray-negative']


plt.subplot(2,2,1)
plt.title(title[0])
plt.imshow(img[0])
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,2)
plt.title(title[1])
plt.imshow(img[1],cmap='gray')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
plt.title(title[2])
plt.imshow(img[2])
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,4)
plt.title(title[3])
plt.imshow(img[3],cmap='gray')
plt.xticks([])
plt.yticks([])

plt.show()