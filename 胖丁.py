# -*- coding: UTF-8 -*-
import numpy as np
import cv2

path = "picture/Pd.jpeg"

Pd = cv2.imread(path)
Pd = cv2.cvtColor(Pd, cv2.COLOR_BGR2BGRA)
b, g, r, a = cv2.split(Pd)
a[:, :] = 0
bgra_Pd_0 = cv2.merge([b, g, r, a])
a[:, :] = 125
bgra_Pd_125 = cv2.merge([b, g, r, a])

# w,h,r = Pd.shape
# Pd[:,:,2] = 255

# Pd = cv2.Canny(Pd, 100, 100)
cv2.imshow("PdCat", Pd)
cv2.imshow("bgra_0", bgra_Pd_0)
cv2.imshow("bgra_125", bgra_Pd_125)

# print("胖丁")

cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("picture/bgr_0.png", bgra_Pd_0)
cv2.imwrite("picture/bgr_125.png", bgra_Pd_125)
