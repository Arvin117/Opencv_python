import numpy as np
import cv2

# img = np.zeros((300,300,3),dtype=np.uint8)
# img[:,0:100,0] = 255
# img[:,100:200,1] = 255
# img[:,200:300,2] = 255
# print("img=\n",img)

''''''
img = cv2.imread("picture/lena.jpg",0)
# #二值化，超过阈值的都为255，不超过的都为0
# r,rst = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# #反二值化，超过阈值的都为0，不超过的都为255
# r,rst = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# #截断阈值化处理，超过阈值的都设置为阈值
r,rst = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# #超阈值零处理，超过阈值的置为0
# r,rst = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
# #低阈值零处理，低于阈值的置为0
# r,rst = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# #自适应阈值处理
t1,thd = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#cv2.ADAPTIVE_THRESH_GAUSSIAN_C，与邻域哥哥像素点到中心点的距离有关，通过高四方程得到各个点的权重值
athdGAUS = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,3)
#cv2.ADAPTIVE_THRESH_MEAN_C，每个点的权重相等
athdMEAN = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,3)

#Ostu,遍历所有阈值，寻找最优的

t,ostu = cv2.threshold(rst,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(t)

cv2.imshow("mean",athdMEAN)
cv2.imshow("gaus",athdGAUS)
# cv2.imshow("rst",rst)
cv2.imshow("img",ostu)
cv2.waitKey()
cv2.destroyAllWindows()