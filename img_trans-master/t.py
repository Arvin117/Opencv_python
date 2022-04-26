import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import cv2

path = "./1gt.png"
img = cv2.imread(path)  # H, W, C
img0 = img[0::2, 0::2, :]
img1 = img[1::2, 0::2, :]
img2 = img[0::2, 1::2, :]
img3 = img[1::2, 1::2, :]

import numpy as np
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1) # 画2行1列个图形的第1个
plt.imshow(img)
plt.axis('off') # 关掉坐标轴为 off
plt.title('image') # 图像题目
fig = plt.figure()
ax2 = fig.add_subplot(2,2,1) # 画2行1列个图形的第2个
plt.imshow(img0)
plt.axis('off') # 关掉坐标轴为 off
plt.title('image0') # 图像题目
ax2 = fig.add_subplot(2,2,2) # 画2行1列个图形的第2个
plt.imshow(img1)
plt.axis('off') # 关掉坐标轴为 off
plt.title('image1') # 图像题目
ax2 = fig.add_subplot(2,2,3) # 画2行1列个图形的第2个
plt.imshow(img2)
plt.axis('off') # 关掉坐标轴为 off
plt.title('image2') # 图像题目
ax2 = fig.add_subplot(2,2,4) # 画2行1列个图形的第2个
plt.imshow(img3)
plt.axis('off') # 关掉坐标轴为 off
plt.title('image3') # 图像题目

plt.show()
