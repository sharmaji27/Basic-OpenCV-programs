import cv2

def emptyfunc():
    pass

path='C:\\Users\\sharma ji\\Pictures\\test\\4.1.01.tiff'

img = cv2.imread(path)
cv2.namedWindow('resizing')
cv2.createTrackbar('x','resizing',500,1000,emptyfunc)
cv2.createTrackbar('y','resizing',500,1000,emptyfunc)

while(1):
    x = cv2.getTrackbarPos('x','resizing')
    y = cv2.getTrackbarPos('y', 'resizing')
    r = cv2.resize(img,None,fx=x/500,fy=y/500,interpolation=cv2.INTER_AREA)
    cv2.imshow('resizing',r)
    if cv2.waitKey(1) ==27:
        break

cv2.destroyAllWindows()

# Interpolation Methods
# INTER_LINEAR
# INTER_NEAREST
# INTER_AREA - best for shrinking
# INTER_CUBIC - best for zooming (interpolation over 4x4 neighborhood)
#INTERLANCZOS4 - best for zooming (interpolation over 8x8 neighborhood)
