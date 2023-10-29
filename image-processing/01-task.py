import cv2 as cv

img=cv.imread('./image.jpeg')

cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()
