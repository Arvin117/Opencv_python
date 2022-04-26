import cv2
import numpy as np
import math

img = cv2.imread("picture/pic_demo.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.normalize(gray, gray, 0, 255, cv2.NORM_MINMAX)
shape = img.shape
print(shape)
img_copy = np.zeros(img.shape[:2])
print(img_copy.shape)
# print(shape[0])
for i in range(shape[0]):
    for j in range(shape[1]):
        img_copy[i, j] = img[i, j, 0] / 3 + img[i, j, 1] / 3 + img[i, j, 2] / 3

print(img[0, 0, 0], img[0, 0, 1], img[0, 0, 2])
print(int(img_copy[0, 0]))
img_copy = np.array(img_copy, np.uint8)

cv2.namedWindow("original", 0)
cv2.resizeWindow("original", 500, 500)
cv2.imshow("original", img)

# cv2.namedWindow("b", 0)
# cv2.resizeWindow("b", 500, 500)
# cv2.imshow("b", b)
# cv2.namedWindow("g", 0)
# cv2.resizeWindow("g", 500, 500)
# cv2.imshow("g", g)
cv2.namedWindow("img_copy", 0)
cv2.resizeWindow("img_copy", 500, 500)
cv2.imshow("img_copy", img_copy)

cv2.namedWindow("gray", 0)
cv2.resizeWindow("gray", 500, 500)
cv2.imshow("gray", gray)
cv2.waitKey()
cv2.destroyAllWindows()
