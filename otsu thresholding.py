import cv2
import matplotlib.pyplot as plt


def main():
    imgpath1 = "C:\\Users\\sharma ji\\Pictures\\test\\7.1.08.tiff"


    img = cv2.imread(imgpath1, 0)


    th = 0
    max_val = 255

    ret, o1 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY+cv2.THRESH_OTSU) #give max value as soon as value crosses threshold
    ret, o2 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) #give max value till it does not crosses threshold
    ret, o3 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO+cv2.THRESH_OTSU) #give 0 value till it does not crosses threshold
    ret, o4 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU) #give 0 as it crosses threshold
    ret, o5 = cv2.threshold(img, th, max_val, cv2.THRESH_TRUNC+cv2.THRESH_OTSU) #give threshold value as it crosses threshold

    output = [img, o1, o2, o3, o4, o5]

    titles = ['Original', 'Binary', 'Binary Inv',
              'Zero', 'Zero Inv', 'Trunc']

    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(output[i],cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main()