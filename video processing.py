import cv2

cam = cv2.VideoCapture(0)
winname = 'live video !!!!'


cv2.namedWindow(winname)

if cam.isOpened():
    ret,frame=cam.read()

else :
    ret=False


while ret:

    ret,frame=cam.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    cv2.imshow(winname, frame)
    cv2.imshow('gray !!', gray)

    k=cv2.waitKey(1)
    if k==27:
        break


cv2.destroyAllWindows()
cam.release()