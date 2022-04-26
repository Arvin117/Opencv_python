import numpy as np
import cv2

path = 'picture/dragon.jpeg'
new_path = 'picture/dragon_grey.jpeg'

# img = cv2.imread(path, cv2.IMREAD_REDUCED_COLOR_2)
img = cv2.imread(path, 0)
# print(img)
cv2.imshow(path, img)

for i in range(10, 100):
    for j in range(80, 100):
        img[i, j] = 255

cv2.imshow("before", img)

k = cv2.waitKey(0)

if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite(new_path, img)
    cv2.destroyAllWindows()
