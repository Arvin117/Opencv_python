import cv2

img = cv2.imread('picture/input.jpeg',0)
target = cv2.imread('picture/target.jpeg',0)
w,h = target.shape

def Gs():
    img_arr = []
    target_arr = []
    temp_img = img.copy()
    temp_target = target.copy()
    img_arr.append(img)
    target_arr.append(target)

    for i in range(1, 4):
        dst_img = cv2.pyrDown(temp_img)
        dst_target = cv2.pyrDown(temp_target)
        img_arr.append(dst_img)
        target_arr.append(dst_target)
        temp_img = dst_img
        temp_target = dst_target
    return img_arr,target_arr

def pp(img_arr,target_arr):
    temp_i = img_arr[3]
    temp_t = target_arr[3]
    point = [0,0]
    py = [0,0]

    for i in range(3,-1,-1):
        tw, th = temp_t.shape
        result = cv2.matchTemplate(temp_i,temp_t,cv2.TM_CCORR_NORMED)
        min_v,max_v,min_loc,max_loc = cv2.minMaxLoc(result)

        point[0] = point[0] * 2 + max_loc[0] - py[0]
        point[1] = point[1] * 2 + max_loc[1] - py[1]
        py[0] = th
        py[1] = tw

        if i == 0:
            cv2.rectangle(img,(point[0],point[1]),(point[0]+h,point[1]+w),(255,0,0),1,8,0)
            cv2.imshow("img",img)
            cv2.waitKey()
            cv2.destroyAllWindows()

        copy = img_arr[i-1].copy()
        temp_i = copy[point[0]*2-tw:point[0]*2+tw*3,point[1]*2-th:point[1]*2+th*3]
        temp_t = target_arr[i-1]

img_arr,target_arr = Gs()
pp(img_arr,target_arr)

#
# '''显示金字塔'''
# for i in range(4):
#     cv2.imshow("a"+str(i),img_arr[i])
#     print(img_arr[i].shape)
#     cv2.imshow("b"+str(i),target_arr[i])
#     print(target_arr[i].shape)




# cv2.imshow("img",img)
# # cv2.imshow("target",target)
# # cv2.imshow("new_img",new_img)
#
# cv2.waitKey()
# cv2.destroyAllWindows()