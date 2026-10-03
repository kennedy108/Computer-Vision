import os
import cv2

img = cv2.imread(os.path.join('.', "data", 'bird.jpg'))

resize_image = cv2.resize(img, (320, 240))

print(img.shape)
print(resize_image.shape)

cv2.imshow('img', img)
cv2.imshow('resize_image', resize_image)

cv2.waitKey(0)
cv2.destroyAllWindows()