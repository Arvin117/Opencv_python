import cv2
import numpy as np

img = cv2.imread("picture/lena.jpg")
rows,cols = img.shape[:2]
print(rows,cols)

'''旋转'''
#中心为远点，逆时针旋转45度，图片缩小0.6倍---->M
M1 = cv2.getRotationMatrix2D((rows/2,cols/2),45,0.6)
# w,h = M.shape[:2]
#旋转
dst1 = cv2.warpAffine(img,M1,(rows,cols))

'''变为平行四边形，指定三个定点，左上，右上，左下'''
#起始点
p1 = np.float32([[0,0],[cols-1,0],[0,rows-1]])
#变换后的三个顶点
p2 = np.float32([[0,rows*0.33],[cols*0.85,rows*0.25],[cols*0.15,rows*0.7]])
#获取变换矩阵M
M2 = cv2.getAffineTransform(p1,p2)
#变身
dst2 = cv2.warpAffine(img,M2,(cols,rows))

'''透视，变为任意四边形，需要四个点的坐标'''
pts1 = np.float32([[0,0],[199,0],[0,199],[199,199]])
pts2 = np.float32([[50,50],[150,50],[50,100],[150,199]])
M3 = cv2.getPerspectiveTransform(pts1,pts2)
dst3 = cv2.warpPerspective(img,M3,(cols,rows))

'''复制'''
mapx = np.zeros(img.shape[0:2],np.float32)
mapy = np.zeros(img.shape[0:2],np.float32)

for i in range(rows):
    for j in range(cols):
        mapx.itemset((i, j),j)
        mapy.itemset((i,j),i)
        #绕x旋转
        # mapx.itemset((i, j), cols - 1 - j)
        #绕y旋转
        # mapy.itemset((i, j), rows - 1 - i)

cp = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
#print(mapx,mapy)


cv2.imshow("dst",dst1)
cv2.imshow("original",img)
cv2.imshow("result",dst2)
cv2.imshow("dst3",dst3)
cv2.imshow("cp",cp)
cv2.waitKey()
cv2.destroyAllWindows()