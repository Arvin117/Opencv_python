import cv2
import imutils
import easyocr

# 预处理
img = cv2.imread('picture/A4.PNG')
# print(img.shape)
img = imutils.resize(img, width=512)
# print(img.shape)
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 边缘检测
img_cn = cv2.bilateralFilter(img_g, 10, 50, 50)  # 双边滤波
img_cn = cv2.Canny(img_cn, 100, 200)
cv2.imshow('cna', img_cn)
cv2.waitKey()
cv2.destroyAllWindows()