import cv2

def emptyfunc():
    pass


winname='video player'
cv2.namedWindow(winname)
path="C:\\Users\\sharma ji\\Pictures\\out.avi"
cam=cv2.VideoCapture(path)
cv2.createTrackbar('speed',winname,1,50,emptyfunc)

while (cam.isOpened()):
    ret,frames=cam.read()
    s = cv2.getTrackbarPos('speed',winname)
    if ret:
        cv2.imshow(winname,frames)
        #1000ms(1 sec) --> 30 frames
        #1000/30ms --> 1 frame
        #delay = 33 (33.33)
        if cv2.waitKey(s)==27:
            break
    else:
        break
