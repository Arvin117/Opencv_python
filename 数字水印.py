import numpy as np
import cv2

path_1 = "picture/Pd.jpeg"
# path_2 = "picture/dragon.jpeg"
path_2 = "picture/水印.jpg"

Pd = cv2.imread(path_1, 0)
sy = cv2.imread(path_2, 0)

Pd = Pd[600:900, 250:650]
sy = sy[200:500, 100:500]
w, h = Pd.shape
# print(Pd.shape)
# print(dragon.shape)
# 提取水印图片的最高位
a = np.ones((w, h), dtype=np.uint8) * 128  # 1000 0000
sy = cv2.bitwise_and(sy, a)
cv2.imshow('o', sy)

# 将提取出得最高位，有效位置为1，方便与之后的待处理图像进行或运算
ShuiY = sy[:, :]
mask = ShuiY[:, :] > 0
ShuiY[mask] = 1  # 0000 0001

# 将待处理图像最低位置0,获取图像的高七位
b = np.ones((w, h), dtype=np.uint8) * 254  # 1111 1110
img = cv2.bitwise_and(Pd, b)

# 添加水印
new_img = cv2.bitwise_or(img, ShuiY)

# 提取水印
c = np.ones((w, h), dtype=np.uint8)  # 0000 0001
new_Shuiy = cv2.bitwise_and(new_img, c)  # 取最后一位（水印）
# 将1置为255 增大对比度
new_mask = new_Shuiy[:, :] > 0
new_Shuiy[new_mask] = 255
# print(new_mask)


cv2.namedWindow("img")
cv2.namedWindow("newimg")
cv2.namedWindow("new_shuiyin")
cv2.moveWindow("img", 0, 0)
cv2.moveWindow("newimg", 500, 0)
cv2.moveWindow("new_shuiyin", 1000, 0)
cv2.imshow("img", img)
cv2.imshow("newimg", new_img)
cv2.imshow("new_shuiyin", new_Shuiy)

# x:250-650 y:600-900
cv2.waitKey()
cv2.destroyAllWindows()
