import cv2

winname = 'record and save !!!!'
cv2.namedWindow(winname)
cam = cv2.VideoCapture(0)

filename = 'C:\\Users\\sharma ji\\Pictures\\out.avi'
codec = cv2.VideoWriter_fourcc('X','V','I','D')
framerate = 30
resolution = (640,480)

save=cv2.VideoWriter(filename,codec,framerate,resolution)

if cam.isOpened():
    ret,frame=cam.read()
else:
    ret=False

while ret:
    ret,frame=cam.read()
    cv2.imshow(winname,frame)
    save.write(frame)
    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()
cam.release()
save.release()
