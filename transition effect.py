import cv2
import numpy as np
import time
path='C:\\Users\\sharma ji\\Pictures\\test\\'

imgpath1= path + '4.2.01.tiff'
imgpath2= path + '4.2.03.tiff'

img1 = cv2.imread(imgpath1)
img2 = cv2.imread(imgpath2)

for i in np.linspace(0,1,100):
    alpha = i
    beta = 1-i
    output = cv2.addWeighted(img1,alpha,img2,beta,0)
    cv2.imshow('transition',output)
    time.sleep(0.05)
    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()