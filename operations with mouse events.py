import cv2
import numpy as np


img = np.zeros((512,512,3),np.uint8)
winname = 'operations'
cv2.namedWindow(winname)

def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),45,(225,225,225),-1)


cv2.setMouseCallback(winname,draw_circle)


def main():
    while(1):
        cv2.imshow(winname,img)
        if cv2.waitKey(1)==27:
            break



if __name__ == '__main__':
    main()