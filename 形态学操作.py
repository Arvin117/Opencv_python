import cv2
import numpy as np

img = cv2.imread("picture/j.png", cv2.IMREAD_UNCHANGED)
lena = cv2.imread("picture/lena.jpg")

cv2.imshow("oimg", img)
mask1 = img[:, :] > 10
mask0 = img[:, :] == 0
img[mask1] = 0
img[mask0] = 255

'''腐蚀cv2.erode( src, kernel ),当kernel全部处于全景里是，中心点为1'''
# kernel = np.array([[1],[1],[1]])
kernel = np.ones((3, 3), np.uint8)
# print(kernel)
dst = cv2.erode(img, kernel, iterations=1)  # iterations 表示循环次数

'''膨胀cv2.dilata( src, kernel ),kernel有一个像素点在前景图像时，中心点置为1'''
dilation1 = cv2.dilate(img, kernel, iterations=1)
dilation2 = cv2.dilate(dst, kernel, iterations=5)

'''                                     形态学操作cv2.morphologyEx( src, op, kernel )
    op:操作类型
        cv2.MORPH_ERODE         腐蚀          腐蚀              erode(src)
        cv2.MORPH_DILATE        膨胀          膨胀              dilate(src)
        cv2.MORPH_OPEN          开运算        先腐蚀后膨胀        dilate(erode(sec))         去燥、计数
        cv2.MORPH_CLOSE         闭运算        先膨胀后腐蚀        erode(dilate(src))         去除内部小孔
        cv2.MORPH_GRADIENT      形态学梯度     膨胀图 - 腐蚀图     dilate(src) - erode(src)   获取前景图像边缘
        cv2.MORPH_TOPHAT        顶帽运算       原始图 - 开运算图   src - open(src)            获取噪声或比原始图像更亮的边缘特征
        cv2.MORPH_BLACKHAT      黑帽运算       闭运算图 - 原始图   close(src) - src           获取内部小孔或比原始图像边缘更暗的部分
        cv2.MORPH_HITMISS       击中击不中     前景、背景 腐蚀图交集 intersection( erode(src), erode(srcI) )
'''

erode = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel, iterations=1)
dilate = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=5)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=5)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel, iterations=1)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel, iterations=5)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel, iterations=5)
# hitmiss = cv2.morphologyEx(img,cv2.MORPH_HITMISS,kernel)

# cv2.imshow("img",img)
# cv2.imshow("opening",opening)
# cv2.imshow("closing",closing)
# cv2.imshow("gradient",gradient)
# cv2.imshow("tophat",tophat)
# cv2.imshow("blackhat",blackhat)
#
# _lena = cv2.morphologyEx(lena,cv2.MORPH_TOPHAT,kernel)
# cv2.imshow("_lena",_lena)
# lena_ = cv2.morphologyEx(lena,cv2.MORPH_BLACKHAT,kernel)
# cv2.imshow("lena_",lena_)

'''                                 核函数cv2.getStructuringElement( shape, ksize )    
    shape:
        cv2.MORPH_RECT          矩形结构元素，所有值为1
        cv2.MORPH_CROSS         十字形结构元素，对角线元素值为1
        cv2.MORPH_ELLIPSE       椭圆形结构元素                         

'''
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
# print(kernel1)
# print(kernel2)
# print(kernel3)
dst1 = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel1, iterations=1)
dst2 = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel2, iterations=1)
dst3 = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel3, iterations=1)

cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)

cv2.waitKey()
cv2.destroyAllWindows()
