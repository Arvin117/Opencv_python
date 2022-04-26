import cv2
import numpy as np

'''                                                 各种滤波                                        '''

# o = cv2.imread("picture/噪声lena.jpg")
# img = cv2.imread("picture/Black_White.jpg")

o = cv2.imread("picture/demo.png", 0)
'''均值滤波cv2.blur( src, Ksize )'''
blur_r3 = cv2.blur(o, (3, 3))
blur_r5 = cv2.blur(o, (5, 5))
blur_r9 = cv2.blur(o, (9, 9))

'''方框滤波cv2.boxFilter( src, ddepth, Ksize [,normalize]),normalize默认为1，表示加和取平均，0表示加和'''
boxF_r3 = cv2.boxFilter(o, -1, (2, 2), normalize=0)
boxF_r5 = cv2.boxFilter(o, -1, (5, 5), normalize=1)
boxF_r9 = cv2.boxFilter(o, -1, (9, 9), normalize=1)

'''高斯滤波cv2.GaussianBlur( src, Ksize, 0, 0),每个Ksize有不同的权重'''
Gs_r3 = cv2.GaussianBlur(o, (3, 3), 0, 0)
Gs_r5 = cv2.GaussianBlur(o, (5, 5), 0, 0)
Gs_r9 = cv2.GaussianBlur(o, (9, 9), 0, 0)

'''中值滤波cv2.medianBlur( src, Ksize ),取K范围内的所有值，然后排序取中间的值作为目标值'''
mdb_r3 = cv2.medianBlur(o, 3)
mdb_r5 = cv2.medianBlur(o, 5)
mdb_r9 = cv2.medianBlur(o, 9)

"r3效果最好"
'''双边滤波cv2.bilateralFilter( src, d, sigmaColor, sigmaSpace[, borderType] ),对于色彩差距大的权重给的小'''
blf_r3 = cv2.bilateralFilter(o, 25, 100, 100)

blf_r5 = cv2.GaussianBlur(o, (5, 5), 0, 0)
blf_r9 = cv2.boxFilter(o, -1, (5, 5))

'''自定义卷积核cv2.filter2D( src, ddepth, kernel ),可以自定义kernel'''
kernel3 = np.ones((3, 3), np.float32) / 9
kernel5 = np.ones((5, 5), np.float32) / 25
kernel9 = np.ones((9, 9), np.float32) / 81

r3 = cv2.filter2D(o, -1, kernel3)
r5 = cv2.filter2D(o, -1, kernel5)
r9 = cv2.filter2D(o, -1, kernel9)

cv2.imshow("original", o)
cv2.imshow("blur", blur_r9)
cv2.imshow("boxFilter", boxF_r9)
cv2.imshow("Gassianblur", Gs_r9)
cv2.imshow("medianblur", mdb_r9)
cv2.imshow("bilateralFilter", blf_r9)

cv2.waitKey()
cv2.destroyAllWindows()
