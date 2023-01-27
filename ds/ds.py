import cv2
import numpy as np
import matplotlib.pyplot as plt

def readmap():
    img = cv2.imread("map.png")
    # dst =cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
    dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('dst', dst)
    # cv2.waitKey(0)
    return dst


map = readmap()
print(map)
# print(map.shape[0])


plt.figure()
plt.imshow(map,'gray')
plt.show()