import numpy as np
import cv2
'''
img1 = np.ones((4,4),dtype=np.uint8)*3
img2 = np.ones((4,4),dtype=np.uint8)*5
img3 = np.ones((4,4),dtype=np.uint8)*66
mask = np.zeros((4,4),dtype=np.uint8)
mask[2:4,2:4] = 1
print("img1 = \n",img1)
print("img2 = \n",img2)
print("img3 = \n",img3)
print("mask = \n",mask)

img3 = cv2.add(img1,img2,mask=mask)
print("img3 = \n",img3)
'''
a = cv2.imread("picture/dragon.jpeg")
w, h, c = a.shape
# print(a.shape)
mask = np.zeros((w,h),dtype=np.uint8)
mask[50:350,200:500] = 255
# mask[100:500,100:200] = 255
c = cv2.bitwise_and(a,a,mask=mask)
print("a.shape = ",a.shape)
print("mask.shape = ",mask.shape)

d = cv2.add(c,(100,100,100,3))#饱和度增加100
cv2.imshow("a",a)
cv2.imshow("mask",mask)
cv2.imshow("c",c)
cv2.imshow("d",d)
cv2.waitKey()
cv2.destroyAllWindows()