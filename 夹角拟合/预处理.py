import cv2
import numpy as np

img_path = "images/12t.jpg"
img = cv2.imread(img_path, 0)

# 去躁:使用双边滤波进行降噪
img_f = cv2.bilateralFilter(img, 25, 100, 100)
# 二值化
# t, img_t = cv2.threshold(img_f, 127, 255, cv2.THRESH_BINARY)
t, img_t = cv2.threshold(img_f, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# 腐蚀膨胀去除内部躁点
kernel = np.ones((3, 3), np.uint8)
img_dilation = cv2.dilate(img_t, kernel, iterations=1)    # 膨胀
img_dst = cv2.erode(img_dilation, kernel, iterations=1)  # 腐蚀
# 找到最大区域并填充
contours, hierarchy = cv2.findContours(img_dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
area = []
for j in range(len(contours)):
    area.append(cv2.contourArea(contours[j]))
max_idx = np.argmax(area)
max_area = cv2.contourArea(contours[max_idx])
for k in range(len(contours)):
    if k != max_idx:
        cv2.fillPoly(img_dst, [contours[k]], 0)
# 边缘检测
img_canny = cv2.Canny(img_dst, 127, 255)

# 双边缘提取
contours, hierarchy = cv2.findContours(img_canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
img_cn_0 = img_canny.copy()
img_cn_0 = cv2.fillPoly(img_cn_0, [contours[0]], 0)
img_cn_1 = img_canny.copy()
img_cn_1 = cv2.fillPoly(img_cn_1, [contours[1]], 0)
# cv2.imshow("img", img_t)
cv2.imshow("imgt", img_canny)
cv2.imshow("imgcn", img_cn_0)
cv2.imshow("imgcn1", img_cn_1)
cv2.waitKey()
cv2.destroyAllWindows()
