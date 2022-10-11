import cv2
import matplotlib.pyplot as plt
path='C:\\Users\\sharma ji\\Pictures\\test\\'

imgpath1 = path + 'download.jpg'
img1 = cv2.imread(imgpath1)

output=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

r,g,b=cv2.split(output)

images=[cv2.merge((r,g,b)),r,g,b]

plt.subplot(2,2,1)
plt.xticks([])
plt.yticks([])
plt.imshow(images[0],cmap='gray')
plt.title('original')

plt.subplot(2,2,2)
plt.xticks([])
plt.yticks([])
plt.imshow(images[1],cmap='Reds')
plt.title('red')

plt.subplot(2,2,3)
plt.xticks([])
plt.yticks([])
plt.imshow(images[2],cmap='Greens')
plt.title('green')

plt.subplot(2,2,4)
plt.xticks([])
plt.yticks([])
plt.imshow(images[3],cmap='Blues')
plt.title('blue')

plt.show()