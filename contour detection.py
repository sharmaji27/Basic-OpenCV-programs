import cv2
import matplotlib.pyplot as plt

winname = 'contour detection'

path = "C:\\Users\\sharma ji\\Pictures\\test\\4.2.07.tiff"
img = cv2.imread(path)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 125, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
org = cv2.imread(path)
org = cv2.cvtColor(org,cv2.cv2.COLOR_BGR2RGB)
cv2.drawContours(img,contours,-1,(0,0,255),1)
titles = ['original','contours']
imgs = [org , img]

for i in range (2):
    plt.subplot(1,2,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.title(titles[i])
    plt.imshow(imgs[i])
plt.show()

# The contour retrieval modes are as follows
# cv2.RETR_EXTERNAL
# cv2.RETR_LIST
# cv2.RETR_CCOMP
# cv2.RETR_TREE
#
# The contour approximation modes are as follows
# cv2.CHAIN_APPROX_NONE
# cv2.CHAIN_APPROX_SIMPLE
# cv2.CHAIN_APPROX_TC89_L1
# cv2.CHAIN_APPROX_TC89_KCOS
