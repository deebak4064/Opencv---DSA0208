import cv2

img = cv2.imread('C:/Documents/Computer Vision/Exp 3.jpg')
edges = cv2.Canny(img, 100, 200)

cv2.imshow('Original Image', img)
cv2.imshow('Canny Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
