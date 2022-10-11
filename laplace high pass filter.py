import cv2
import matplotlib.pyplot as plt


def main():
    imgpath = "C:\\Users\\sharma ji\\Pictures\\test\\7.1.06.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    edges = cv2.Laplacian(img, -1, ksize=5, scale=1, delta=0,
                          borderType=cv2.BORDER_DEFAULT)

    output = [img, edges]
    titles = ['Original', 'Edges']

    for i in range(2):
        plt.subplot(1, 2, i + 1)
        plt.imshow(output[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()


if __name__ == "__main__":
    main()