import cv2

imgpath = "C:\\Users\\sharma ji\\Pictures\\test\\4.1.01.tiff"
img = cv2.imread(imgpath)
cv2.imshow('sharma',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
