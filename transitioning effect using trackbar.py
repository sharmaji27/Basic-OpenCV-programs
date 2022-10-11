import cv2

def emptyfunc():
    pass

path='C:\\Users\\sharma ji\\Pictures\\test\\'

imgpath1 = path + '4.2.01.tiff'
imgpath2 = path + '4.2.03.tiff'

img1 = cv2.imread(imgpath1)
img2 = cv2.imread(imgpath2)

winname = 'transitioning'
cv2.namedWindow(winname)

cv2.createTrackbar('alpha',winname,0,1000,emptyfunc)

while(1):
    alpha = cv2.getTrackbarPos('alpha',winname)/1000
    beta=1-alpha
    output = cv2.addWeighted(img1, alpha, img2, beta, 0)
    cv2.imshow(winname,output)
    print(alpha,beta)
    k=cv2.waitKey(1)
    if k==27:
        break