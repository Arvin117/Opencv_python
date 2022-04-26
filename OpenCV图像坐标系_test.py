import numpy as np
import cv2

img = cv2.imread('picture/dragon.jpeg', cv2.IMREAD_UNCHANGED)
''' 
cv2.IMREAD_COLOR : 默认使用该种标识。加载一张彩色图片，忽视它的透明度。
cv2.IMREAD_GRAYSCALE : 加载一张灰度图。
cv2.IMREAD_UNCHANGED : 加载图像，包括它的Alpha通道。
觉得麻烦可以用 1， 0 ，-1代替
'''
print("img.shape:", img.shape)
'''
img.shape[0]：图像的垂直尺寸（高度）
img.shape[1]：图像的水平尺寸（宽度）
（也可以用于矩阵）
img.shape[2]：图像的通道数
啥也不写默认三个全部打印
'''
logo = cv2.imread('picture/opencv_logo.jpg', cv2.IMREAD_UNCHANGED)
logo = cv2.resize(logo, (20, 20))
print("logo.shape:", logo.shape)
butterfly = cv2.imread('picture/butterfly.jpg', cv2.IMREAD_UNCHANGED)
butterfly = cv2.resize(butterfly, (20, 20))
print("butterfly.shape:", butterfly.shape)

cv2.imshow('src', img)
cv2.moveWindow('src', 0, 0)
#cv2.namedWindow('src', 0)

#read color values at position y, x
y = 100
x = 50
(b, g, r) = img[y, x]
#print color valuer to screen
print('bgr:', b, g, r)

#先行后列
#img[y:y+height, x:width]
img[100:100 + logo.shape[0], 300:300 + logo.shape[1]] = logo[:, :, 0:3] #两张图片的shape不一样
img[300:300 + logo.shape[1], 100:100 + logo.shape[0]] = butterfly[:, :, 0:3]

#给图像添加字体
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(img, text='col=width=X0,row=height-Y0', org=(0, 0), fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2, bottomLeftOrigin=True)
cv2.putText(img, text='col=width=X10,row=height-Y30', org=(10, 30), fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2, bottomLeftOrigin=True)
cv2.putText(img, text='col=width=X100,row=height-Y300', org=(100, 300), fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2, bottomLeftOrigin=True)
cv2.putText(img, text='col=width=X300,row=height-Y100', org=(300, 100), fontFace=font, fontScale=0.5, color=(0, 255, 0), thickness=2, bottomLeftOrigin=True)

cv2.imshow('img+logo', img)
cv2.imwrite('picture/img_logo.jpg', img)
cv2.moveWindow('img+logo', x=img.shape[0], y=0)

if cv2.waitKey(10000) & 0xFF == ord('q'):
    cv2.destroyAllWindows()