import cv2
import matplotlib.pyplot as plt


def main():
    imgpath = "C:\\Users\\sharma ji\\Pictures\\test\\5.1.13.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    edgesx = cv2.Sobel(img,-1,dx=1,dy=0,ksize=1)
    edgesy= cv2.Sobel(img, -1, dx=0, dy=1, ksize=1)
    edges = edgesx + edgesy
    output = [img, edgesx ,edgesy,edges]
    titles = ['Original','x','y' ,'Edges']

    for i in range(4):
        plt.subplot(2, 2, i + 1)
        plt.imshow(output[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()


if __name__ == "__main__":
    main()