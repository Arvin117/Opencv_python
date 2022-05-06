import cv2
import numpy as np


def video_mirror_output(video):
    new_img = np.zeros_like(video)
    h, w = video.shape[0], video.shape[1]
    for row in range(h):
        for i in range(w):
            new_img[row, i] = video[row, w - i - 1]
    return new_img


cam = cv2.VideoCapture(0)  # 调用摄像头
Obj_low = np.array([0, 0, 0])
Obj_high = np.array([179, 157, 79])
while True:
    # 镜像
    ret, frame = cam.read()
    if ret == True:
        new_video = cv2.flip(frame, 180)
    img = new_video
    # img = cam.read()[1]
    img = cv2.resize(img, (800, 600))
    blur_img = cv2.GaussianBlur(img, (21, 21), 0)  # 归一化，模糊图像，使得像素分布均匀
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    MASK1 = cv2.inRange(HSV, Obj_low, Obj_high)  # 二值化，中间阈值为255，其余为0
    MASK1 = cv2.erode(MASK1, None, iterations=2)
    MASK1 = cv2.dilate(MASK1, None, iterations=2)
    contours, hierarchy = cv2.findContours(MASK1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    center = None
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)  # 选取面积最大的区域
        ((x, y), radius) = cv2.minEnclosingCircle(c)    # 返回值为圆心x，y 和半径
        # M = cv2.moments(c)
        # center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))   # 圆心
        center = (int(x), int(y))
        if radius > 10:
            cv2.circle(img, center, 5, (0, 0, 255), -1)
            cv2.circle(img, center, int(radius), (0, 0, 255), 2)
    cv2.imshow("my window", img)
    k = cv2.waitKey(1)
    if k == 27:
        break
cam.release()
cv2.destroyAllWindows()
