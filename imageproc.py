import cv2

img = cv2.imread('fast.png')

cv2.imshow('1', img)
img2 = img
img2 = cv2.bilateralFilter(img, 9, 20, 10)

cv2.imshow('2', img2)

cv2.waitKey(0)
