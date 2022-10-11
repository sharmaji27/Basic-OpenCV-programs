import cv2
import matplotlib.pyplot as plt
import numpy as np


def main():
    imgpath1 = "C:\\Users\\sharma ji\\Pictures\\gymboiiss (2).png"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

    rows, columns, channels = img1.shape

    point1 = np.float32([[0, 0], [400, 0], [0, 400], [400, 400]])
    point2 = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])

    P = cv2.getPerspectiveTransform(point1, point2)

    print(P)

    output = cv2.warpPerspective(img1, P, (700, 700))

    plt.imshow(output)
    plt.title('Changed Perspective')
    plt.show()


if __name__ == "__main__":
    main()