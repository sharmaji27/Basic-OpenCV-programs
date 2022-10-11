import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
winname='shapes'
cv2.circle(img , (206,206) , 50 , (225,225,225) , -1)
cv2.rectangle(img,(20,40),(160,140),(225,225,225),-1)
cv2.ellipse(img,(380,380),(50,20),0,0,360,(225,225,225),-1)
cv2.line(img,(0,0),(512,512),(0,225,0))
cv2.imshow(winname,img)
cv2.waitKey(0)
cv2.destroyAllWindows()
