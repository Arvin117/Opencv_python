import cv2
import numpy as np

lena = cv2.imread("picture/lena.jpg", 0)
w, h = lena.shape
a = np.zeros((w, h, 8), dtype=np.uint8)

# 创建位平面分解层 0000 0001，0000 0010，0000 0100。。。。。。。1000 0000
for i in range(8):
    a[:, :, i] = 2 ** i

print(a)
b = np.zeros((w, h, 8), dtype=np.uint8)
cv2.imshow("lena", lena)
for i in range(8):
    # 存储各位平面
    b[:, :, i] = cv2.bitwise_and(lena, a[:, :, i])
    # 将图像像素>0的点变为255，增大对比度
    mask = b[:, :, i] > 0
    b[mask] = 255
    cv2.imshow(str(i), b[:, :, i])

cv2.waitKey()
cv2.destroyAllWindows()
