import numpy as np
import cv2

a = cv2.imread("picture/lena.jpg")
c = cv2.imread("picture/lena.jpg",0)
b = a

print(a.shape)
#超过255的话 对256进行取余
result1 = a + b
#超过255的直接记为255
result2 = cv2.add(a,b)

cv2.imshow("+",result1)
cv2.imshow("add",result2)

#加权，两个图像必须大小、类型相同
d = cv2.addWeighted(a,0.6,result1,0.4,0)

cv2.imshow("addW",d)
cv2.waitKey()
cv2.destroyAllWindows()