import cv2
import numpy as np

imgpath="C:\\Users\\sharma ji\\Pictures\\gymboiiss (2).png"
winname='shifting !!'
img = cv2.imread(imgpath)

row,col,channels = img.shape
t=np.float32([[1,0,-50],[0,1,50]]) #1's are for zooming effect in respective axes

shifted_image = cv2.warpAffine(img,t,(col,row))

cv2.imshow(winname,shifted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()