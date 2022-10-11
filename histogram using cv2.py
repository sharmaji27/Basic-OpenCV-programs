import cv2
import matplotlib.pyplot as plt

imgpath = "C:\\Users\\sharma ji\\Pictures\\test\\4.2.07.tiff"
img = cv2.imread(imgpath)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

red_hist = cv2.calcHist([img],[0],None,[256],[0,255])
green_hist = cv2.calcHist([img],[1],None,[256],[0,255])
blue_hist = cv2.calcHist([img],[2],None,[256],[0,255])

plt.subplot(4,1,1)
plt.imshow(img)
plt.title('image')
plt.xticks([])
plt.yticks([])

plt.subplot(4,1,2)
plt.plot(red_hist,color='r')
plt.xlim([0,255])
plt.title('red histogram')

plt.subplot(4,1,3)
plt.plot(green_hist,color='g')
plt.xlim([0,255])
plt.title('green histogram')

plt.subplot(4,1,4)
plt.plot(blue_hist,color='b')
plt.xlim([0,255])
plt.title('blue histogram')

plt.show()