import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'whiteboard.png'))

print(img.shape)

#lines
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)

#rectangle
cv2.rectangle(img, (30, 45), (70, 80), (0, 0, 255), -1)

#circle
cv2.circle(img, (70, 95), 15, (255,0,0), -1)

#text
cv2.putText(img, 'Hey', (110, 130), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,0), 3)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()