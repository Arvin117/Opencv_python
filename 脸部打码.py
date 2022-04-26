import numpy as np
import cv2

Pd = cv2.imread("picture/Pd.jpeg",0)
#cat = Pd[0:800,500:1100]
#face = Pd[600:900,250:650]
Pd = Pd[500:1100,0:800]
w,h = Pd.shape

#打码的脸部区域
mask = np.zeros((w,h),dtype=np.uint8)
mask[40:450,200:680] = 255
#反色区域
_mask = cv2.bitwise_not(mask)

face = cv2.bitwise_and(Pd,mask)#取脸
bg = cv2.bitwise_and(Pd,_mask)#取其他

#打码
key = np.random.randint(0,255,(w,h),dtype=np.uint8)
new_Pd = cv2.bitwise_xor(Pd,key)
new_face = cv2.bitwise_and(new_Pd,mask)
new_Pd = new_face + bg

#解码
past_Pd = cv2.bitwise_xor(new_Pd,key)#解码
past_face = cv2.bitwise_and(past_Pd,mask)#背景打码部分置0
past_bg = cv2.bitwise_and(new_Pd,_mask)#背景
now_Pd = past_face + past_bg

cv2.imshow("Pd_cat",new_Pd)
cv2.moveWindow("Pd_cat",0,0)
cv2.imshow("face",now_Pd)
cv2.moveWindow("face",500,0)
cv2.waitKey()
cv2.destroyAllWindows()

