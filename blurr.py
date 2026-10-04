import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'tiger-salt-pepper.png'))

k_size = 7 #larger the number the bigger the average (strong the blur)
img_blur = cv2.blur(img, (k_size, k_size))
img_guassian = cv2.GaussianBlur(img, (k_size, k_size), 5)
img_median = cv2.medianBlur(img, k_size)

cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gussian', img_guassian)
cv2.imshow('img_median', img_median)

cv2.waitKey(0)
cv2.destroyAllWindows()