import cv2
import numpy as np

opencv = cv2.imread("picture/opencv_logo.jpg")
hsv = cv2.cvtColor(opencv,cv2.COLOR_BGR2HSV)

Blue_min = np.array([110,50,50])
Blue_max = np.array([130,255,255])
Green_min = np.array([50,50,50])
Green_max = np.array([70,255,255])
Red_min = np.array([0,50,50])
Red_max = np.array([30,255,255])

mask_b = cv2.inRange(hsv,Blue_min,Blue_max)
Blue = cv2.bitwise_and(opencv,opencv,mask=mask_b)
mask_g = cv2.inRange(hsv,Green_min,Green_max)
Green = cv2.bitwise_and(opencv,opencv,mask=mask_g)
mask_r = cv2.inRange(hsv,Red_min,Red_max)
Red = cv2.bitwise_and(opencv,opencv,mask=mask_r)
# color_mask = Blue[:,:] == 0
# Blue[color_mask] = 255

cv2.imshow("img",opencv)
cv2.imshow("Blue",Blue)
cv2.imshow("Green",Green)
cv2.imshow("Red",Red)
cv2.waitKey()
cv2.destroyAllWindows()