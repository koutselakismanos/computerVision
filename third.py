import numpy as np
import cv2

cap = cv2.VideoCapture(0)
img = cv2.imread('watch.jpeg', cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (150, 150), (0, 0, 0), 1)

cv2.rectangle(img, (15, 25), (200, 150), (0, 0, 0), 1)
cv2.circle(img, (200, 200), 30, (0, 255, 0), 2)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 0, 255), 2)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV TUTS', (0, 130), font, 1, (255, 100, 0), 2)

while True:
    ret, frame = cap.read()
    cv2.putText(frame, 'OpenCV TUTS', (0, 130), font, 1, (255, 100, 0), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(cv2.waitKey(1) & 0xFF)
        break


cap.release()
# cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
