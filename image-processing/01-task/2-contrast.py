import cv2 as cv
import numpy as np

img = cv.imread('./contrast.jpeg')

# first-alogrithm => Histogram Equalization
gray_scale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
equ_image=cv.equalizeHist(gray_scale)


# 02-> contrast stratching
minOriginal = img.min()
maxOriginal = img.max()

minDesired = 0
maxDesired = 255
width, height, *_ = np.shape(img)

cv.imshow("img before contrast", img)
# img_stratches = (img - minOriginal) * ((maxDesired - minDesired) / (maxOriginal - minOriginal))+ minDesired
for i in range(width):
  for j in range(height):
       img[i][j] = img[i][j] * 2

# print(img_stratches)
cv.imshow("img after contrast", img)

# cv.imshow("img_stratches", img_stratches)

 

# cv.imshow("Image before Contrast", img)
# cv.imshow("gray-scale", gray_scale)
# cv.imshow("gray-equ", equ_image)


cv.waitKey(0)
cv.destroyAllWindows()

# cv.imwrite('./contrast-gray.jpeg', equ_image)
