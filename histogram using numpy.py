import cv2
import matplotlib.pyplot as plt
import numpy as np

imgpath = "C:\\Users\\sharma ji\\Pictures\\test\\4.2.07.tiff"
img = cv2.imread(imgpath,0)

plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.title('image')
plt.xticks([])
plt.yticks([])

plt.subplot(1,2,2)
hist,bin = np.histogram(img.ravel(),256,[0,255])
plt.xlim([0,255])
plt.plot(hist)
plt.title('histogram')
plt.show()