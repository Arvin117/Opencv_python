import cv2
import numpy as np

kernel1 = np.array([[1, 1, 1],
                   [0, 0, 0],
                   [-1, -1, -1]]) * 2
kernel2 = np.array([[1/4, 1/4],
                   [1/4, 1/4]])
kernel3 = np.array([[-1, 0, 1],
                   [-1, 0, 1],
                   [-1, 0, 1]]) * 2


o = cv2.imread("picture/lena.jpg")

r1 = cv2.filter2D(o, -1, kernel1)
r2 = cv2.filter2D(o, -1, kernel3)
r3 = r1 + r2
r3 = cv2.cvtColor(r3, cv2.COLOR_BGR2GRAY)

cv2.imshow("original", o)
cv2.imshow("result1", r1)
cv2.imshow("result2", r2)
cv2.imshow("result3", r3)
cv2.waitKey()
cv2.destroyAllWindows()

