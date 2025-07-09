import cv2
image = cv2.imread("C:\\Users\\shanm\\Pictures\\Screenshots\\Screenshot 2025-06-29 165134.png")
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotated 90° Clockwise", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
