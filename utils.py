import cv2
import numpy as np
# import scipy.interpolate

# path = "picture/Pd.jpeg"
# img = cv2.imread(path)
#
# img_new = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#
# cv2.imshow("img",img)
# cv2.imshow("gray",img_new)
# cv2.waitKey()
# cv2.destroyAllWindows()
#
# print(img_new[1,0])
# value = img[1,0,0]*0.114 + img[1,0,1]*0.587 + img[1,0,2]*0.299
# print(value)
# #
# # key = np.random.randint(0,255,(2,4),dtype=np.uint8)
# # color_key = cv2.cvtColor(key,cv2.COLOR_GRAY2BGR)
# # cv2.imshow("key",key)
# # cv2.imshow("color_key",color_key)

img_blue = np.zeros((1,1,3),dtype=np.uint8)
img_green = np.zeros((1,1,3),dtype=np.uint8)
img_red = np.zeros((1,1,3),dtype=np.uint8)

img_blue[0,0,0] = 255
img_green[0,0,1] = 255
img_red[0,0,2] = 255

hsv_blue = cv2.cvtColor(img_blue,cv2.COLOR_BGR2HSV)
hsv_green = cv2.cvtColor(img_green,cv2.COLOR_BGR2HSV)
hsv_red = cv2.cvtColor(img_red,cv2.COLOR_BGR2HSV)

print(hsv_blue)
# print(img_blue)
hsv_blue[0,0,1] = 0
print(hsv_blue)

# cv2.imshow("img_b",img_blue)
# cv2.imshow("img_g",img_green)
# cv2.imshow("img_r",img_red)
cv2.imshow("hsv_b",hsv_blue)
# cv2.imshow("hsv_g",hsv_green)
# cv2.imshow("hsv_r",hsv_red)
#
# cv2.moveWindow("img_b",0,0)
# cv2.moveWindow("img_g",0,200)
# cv2.moveWindow("img_r",0,400)
# cv2.moveWindow("hsv_b",400,0)
# cv2.moveWindow("hsv_g",400,200)
# cv2.moveWindow("hsv_r",400,400)

cv2.waitKey()
cv2.destroyAllWindows()