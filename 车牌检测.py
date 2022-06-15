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
# cv2.imshow('cna', img_cn)
# cv2.waitKey()
# cv2.destroyAllWindows()


# 寻找闭合图像
contours, hierarchy = cv2.findContours(img_cn.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img_copy = img.copy()
cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 3)

# 对闭合区域进行排序，删除干扰项
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:15]
img_cp = img.copy()
cv2.drawContours(img_cp, contours, -1, (0, 255, 0), 3)
cv2.imshow('a', img_cp)
# 寻找矩形区域
img_contour = None
for contour in contours:
    # 封闭区域周长
    arclength = cv2.arcLength(contour, True)
    approx_dist = 0.01 * arclength
    # cv.approxPolyDP() 的参数1是源图像的某个轮廓；参数2(epsilon)是一个距离值，
    # 表示多边形的轮廓接近实际轮廓的程度，值越小，越精确；参数3表示是否闭合。
    # 返回值为拟合的多边形的角点
    approx_contour = cv2.approxPolyDP(contour, approx_dist, True)
    if len(approx_contour) == 4:
        img_contour = approx_contour
        x, y, w, h = cv2.boundingRect(contour)
        img_crop = img[y: y + h, x: x + w]
        local_x, local_y = x, y

cv2.drawContours(img, [img_contour], -1, (0, 255, 0), 3)

#  车牌字母识别
reader = easyocr.Reader(['ch_sim','en'])
t = reader.readtext(img_crop)
print(t)
p = ''
for i in t:
    word = i[1]
    p += word
print(p)
cv2.putText(img, p, (local_x + 20, local_y + 60), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)

# cv2.imshow('A4_cn', img_crop)
cv2.imshow('A4_ct', img)
cv2.waitKey()
cv2.destroyAllWindows()
