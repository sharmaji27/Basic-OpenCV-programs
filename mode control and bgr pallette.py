import cv2
import numpy as np


mode=True
drawing=False
(ix,iy) = (-1,-1)

def emptyfunc():
    pass


img = np.zeros((512,512,3),np.uint8)
winname = 'testing'
cv2.namedWindow(winname)

cv2.createTrackbar('B',winname,0,255,emptyfunc)
cv2.createTrackbar('G',winname,0,255,emptyfunc)
cv2.createTrackbar('R',winname,0,255,emptyfunc)





def draw_shapes(event,x,y,flags,param):

    global mode,drawing,ix,iy

    blue = cv2.getTrackbarPos('B', winname)
    green = cv2.getTrackbarPos('G', winname)
    red = cv2.getTrackbarPos('R', winname)


    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(x,y),(ix,iy),(blue,green,red),-1)
            else:
                cv2.circle(img,(x, y),10,(blue,green,red), -1)

    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False







cv2.setMouseCallback(winname,draw_shapes)



def main():
    global mode
    while(1):
        cv2.imshow(winname,img)
        k=cv2.waitKey(1)
        if k==27:
            break
        elif k==ord('m') or k==ord('M'):
            mode=not mode



if __name__ == '__main__':
    main()

