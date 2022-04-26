import numpy as np
import cv2

path = "picture/Pd.jpeg"

img = cv2.imread(path,0)
w,h = img.shape
a = np.random.randint(0,255,(w,h),dtype=np.uint8) #密钥
cv2.imshow("key",a)
b = cv2.bitwise_xor(img,a)#加密
cv2.imshow("Encryption",b)
c = cv2.bitwise_xor(b,a)#解密
cv2.imshow("Decryption",c)

cv2.waitKey()
cv2.destroyAllWindows()
