import cv2
import time

imgpath="C:\\Users\\sharma ji\\Pictures\\gymboiiss (2).png"
winname='rotating image !!'
img = cv2.imread(imgpath)

row,col,channels = img.shape
angle=360
scale=0.1
while(1):
    angle-=1
    time.sleep(0.01)
    if angle==0:
        angle=360
    scale+=0.05
    if scale>2:
        scale=0.05
    r = cv2.getRotationMatrix2D((col/2,row/2),angle,scale)
    shifted_image = cv2.warpAffine(img,r,(col,row))
    cv2.imshow(winname,shifted_image)
    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()