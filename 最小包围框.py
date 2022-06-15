import cv2
import numpy as np

img = cv2.imread('picture/cc.jpg')
cv2.imshow("original", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
'''最小包围矩形框'''
rect = cv2.minAreaRect(contours[0])
print("返回值rect：\n", rect)
points = cv2.boxPoints(rect)  # 转换类型
print("转换后的points:\n", points)
points = np.int0(points)  # 取整
cv2.drawContours(img, [points], 0, (255, 255, 255), 2)
cv2.imshow("result", img)

print("面积为：", cv2.contourArea(contours[0]))

'''最优拟合椭圆'''
ellipse = cv2.fitEllipse(contours[0])
cv2.ellipse(img, ellipse, (0, 255, 0), 3)
print("ellipse=", ellipse)
cv2.imshow("ellipse", img)

'''凸包'''
img = cv2.imread("picture/cc.jpg")
mask0 = img[:, :] > 100
mask1 = img[:, :] < 100
img[mask0] = 255
img[mask1] = 0
kernel = np.ones((3, 3), np.uint8)
img = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel, iterations=1)
img = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel, iterations=1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
hull = cv2.convexHull(contours[0])  # 返回坐标值
# hull2 = cv2.convexHull(contours[0], returnPoints=False) #返回索引值
print(hull)
cv2.polylines(img, [hull], True, (0, 255, 0), 2)
cv2.imshow("凸包", img)

cv2.waitKey()
cv2.destroyAllWindows()
