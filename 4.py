import numpy as np
import cv2

img = cv2.imread('watch.jpeg', cv2.IMREAD_COLOR)

img[10, 10] = [0, 0, 0]

px = img[10, 10]
print(px)

# img[100:150, 100:150] = img[200:150, 200: 150]
watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow('yy', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
