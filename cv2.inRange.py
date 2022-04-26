import cv2
import numpy as np

img = np.random.randint(0,256,(5,5),dtype=np.uint8)
min = 130
max = 255
#如果在区间min和max中，则值输出为255，不在输出0
mask = cv2.inRange(img,min,max)
print("img=\n",img)
print("mask=\n",mask)

cv2.imshow("i",img)
cv2.imshow("ii",mask)


cv2.waitKey()
cv2.destroyAllWindows()