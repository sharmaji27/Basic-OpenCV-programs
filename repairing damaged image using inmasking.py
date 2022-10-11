import cv2
import matplotlib.pyplot as plt

damaged_image_path = "C:\\Users\\sharma ji\\Pictures\\test\\Damaged Image.tiff"
mask_path = "C:\\Users\\sharma ji\\Pictures\\test\\Mask.tiff"

damaged_image = cv2.imread(damaged_image_path)
mask = cv2.imread(mask_path,0)
damaged_image=cv2.cvtColor(damaged_image,cv2.COLOR_BGR2RGB)

output1 = cv2.inpaint(damaged_image,mask,1,cv2.INPAINT_TELEA)
output2 = cv2.inpaint(damaged_image,mask,1,cv2.INPAINT_NS)

img=[damaged_image,mask,output1,output2]
titles=['damaged image','mask','TELEA','NS']

for i in range (4):
    plt.subplot(2,2,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.title(titles[i])
    plt.imshow(img[i])
plt.show()