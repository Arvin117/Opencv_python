import cv2
import matplotlib.pyplot as plt
import numpy as np

path = "picture/#.png"
path = "picture/lena.jpg"
# img = cv2.imread(path,cv2.IMREAD_UNCHANGED)
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

'''Sobel算子cv2.Sobel( src, ddepth, dx, dy[, ksize[, delta[, borderType]]]] )  
    ddepth通常为cv2.CV_64F,之后要对结果取绝对值      kisze:Sobel核的大小，该值位-1时表示用Scharr运算 
    取绝对值： dst = convertScaleAbs( src[, alpha,[, beta]] )      ==>  dst = saturate( src*alpha + beta )超过255取255
                
                -1  0   1                       -1  -2  -1
    Soble_x =   -2  0   2         Sobel_y =     0   0   0
                -1  0   1                       1   2   1
'''
arr = np.random.randint(-256, 256, (4, 4), dtype=np.int16)
rst = cv2.convertScaleAbs(arr)

'''如果参数dx或者dy为1时，只得到了图像黑色框的右边界。这是因为，左边界在运算时得到了负值，所以被置为0，显示为黑色。
    若想要显示出来，必须将ddepth的值设置为跟大范围的数据结构类型，并将其映射到8位图像内
        也可以将dx或者dy的值设为2，但是边界会变窄
    '''
dst_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # x方向梯度，x方向颜色发生跳跃时置为1
dst_x = cv2.convertScaleAbs(dst_x)
dst_y = cv2.Sobel(img, -1, 0, 2, ksize=3)  # y方向梯度，y方向颜色发生跳跃时置为1

dst = cv2.addWeighted(dst_x, 0.5, dst_y, 0.5, 0)  # 将dst_x和dst_y叠加

cv2.imshow("dst_Sobel", dst)

dst_xy = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)  # xy方向梯度的交点
dst_xy = cv2.convertScaleAbs(dst_xy)

'''     
                cv2.Sobel(img,ddepth,dx,dy,-1)   ==   cv2.Scharr(img,ddepth,dx,dy)
Scharr算子cv2.Scharr( src, ddepth, dx, dy[, scale[, delta[, borderType]]] )
scale:缩放因子，默认位1。        delta：亮度值，默认为0          borderType：边界样式
一般格式:cv2.Scharr( src,ddepth, dx, dy)        or          cv2.Scharr( src,ddepth, dx, dy, -1)

                  -3   0   3                            -3  -10 -3
    Scharr_x  =   -10  0   10            Scharr_y  =     0   0   0
                  -3   0   3                             3   10  3 
'''

dst_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)
dst_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)
# dst_xy = cv2.Scharr(img,cv2.CV_64F,1,1)

dst_x = cv2.convertScaleAbs(dst_x)
dst_y = cv2.convertScaleAbs(dst_y)
# dst_xy = cv2.convertScaleAbs(dst_xy)
#
dst = cv2.addWeighted(dst_x, 0.5, dst_y, 0.5, 0)

# cv2.imshow("img",img)
# cv2.imshow("Sobel_x",dst_x)
# cv2.imshow("Sobel_y",dst_y)
# cv2.imshow("Sobel_xy",dst_xy)
cv2.imshow("dst_Scharr", dst)

'''     
                            边缘锐化（边缘检测）
        Laplacian算子:二阶导数算子，旋转不变性。通常系数之和为 0
        cv2.Laplacian( src, ddepth,[, ksize[, scale[, delta[, borderType]]]] )
        ksize = 1时，采用 3*3 的核
        
                       0    1   0          
        Laplacian  =   1    -4  1             
                       0    1   0

'''
Laplacian = cv2.Laplacian(img, cv2.CV_64F)
Laplacian = cv2.convertScaleAbs(Laplacian)

cv2.imshow("Laplacian", Laplacian)

# '''         直方图     '''
# plt.hist(img.ravel(),256)

cv2.waitKey()
cv2.destroyAllWindows()
