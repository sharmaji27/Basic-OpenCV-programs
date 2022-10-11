import cv2

mode=True

winname = 'webcam resolution !!'
cv2.namedWindow(winname)
cam = cv2.VideoCapture(0)

print('width : '+ str(cam.get(3)))
print('height : '+ str(cam.get(4)))

cam.set(3,1280)
cam.set(4,720)

print('width : '+ str(cam.get(3)))
print('height : '+ str(cam.get(4)))

if cam.isOpened():
    ret,frame=cam.read()
else:
    ret=False

while ret:
    converted=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,frame=cam.read()
    if mode==True:
        cv2.imshow(winname,frame)
    else:
        cv2.imshow('gray', converted)
    k=cv2.waitKey(1)
    if k== 27:
        break
    elif k==ord('M') or k==ord('m'):
        mode=not mode

cam.release()