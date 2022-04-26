import cv2
import numpy as np
import os

# Make an array of 120,000 random bytes.
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = np.array(randomByteArray)

# Convert the array to make a 400*300 grayscale image.
# numpy.random.randint(0, 256, 120000).reshape(300, 400)
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('picture/RandomGray.png', grayImage)

# Convert the array to make a 400*100 color image.
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('picture/RandomColor.png', bgrImage)

