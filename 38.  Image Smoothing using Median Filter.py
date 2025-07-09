import cv2

img = cv2.imread('Exp 3.jpg')
median = cv2.medianBlur(img, 5)

cv2.imshow('Original Image', img)
cv2.imshow('Median Blurred Image', median)
cv2.waitKey(0)
cv2.destroyAllWindows()
