import cv2
import matplotlib.pyplot as plt


def main():
    imgpath1 = "C:\\Users\\sharma ji\\Pictures\\test\\gray21.512.tiff"


    img = cv2.imread(imgpath1, 1)


    th = 127
    max_val = 255

    ret, o1 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY) #give max value as soon as value crosses threshold
    ret, o2 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV) #give max value till it does not crosses threshold
    ret, o3 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO) #give 0 value till it does not crosses threshold
    ret, o4 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO_INV) #give 0 as it crosses threshold
    ret, o5 = cv2.threshold(img, th, max_val, cv2.THRESH_TRUNC) #give threshold value as it crosses threshold

    output = [img, o1, o2, o3, o4, o5]

    titles = ['Original', 'Binary', 'Binary Inv',
              'Zero', 'Zero Inv', 'Trunc']

    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main()