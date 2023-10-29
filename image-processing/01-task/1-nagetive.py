
import cv2 as cv
import numpy as np

img = cv.imread('./image.jpeg')


# first_alogrithm
imgNagetive = 255 - img

# width, height = np.shape(img)
# scond_alogrithm
width, height, *_ = np.shape(img)
print(width, height)
cv.imshow("Image before Nagetive", img)
for row in range(width):
    for col in range(height):
        img[row, col] = 255 - img[row, col]

cv.imshow("Image after Nagetive", img)
cv.imshow("Image after Nagetive_2", imgNagetive)


cv.waitKey(0)
cv.destroyAllWindows()