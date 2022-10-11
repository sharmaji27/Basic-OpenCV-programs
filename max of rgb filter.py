import cv2
import numpy as np

w = 800
h = 600

winname = 'live video feed'
cv2.namedWindow(winname)
cam = cv2.VideoCapture(0)

cam.set(3,w)
cam.set(4,h)

if cam.isOpened():
    ret, frame = cam.read()
else:
    ret=False

while (ret):
    ret,frame = cam.read()
    r,g,b = cv2.split(frame)
    max = np.maximum(np.maximum(r,g),b)
    r[r < max] = 0
    b[b < max] = 0
    g[g < max] = 0
    print(r,g,b)
    output = cv2.merge((r,g,b))
    cv2.imshow(winname,output)

    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()
cam.release()
