import cv2
import numpy as np
def main ():
    events = [i for i in dir(cv2) if 'EVENT' in i]




    print (events)

if __name__ == '__main__':
    main()