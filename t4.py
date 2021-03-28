import cv2



im = cv2.imread('C:\\Users\\Singal\\Pictures\\ice age.jpg')
print(im.shape)
cv2.imshow("img",im)
cv2.waitKey(0)

