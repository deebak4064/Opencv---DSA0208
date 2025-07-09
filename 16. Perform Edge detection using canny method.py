import cv2
import numpy as np
image = cv2.imread("C:\\Users\\shanm\\Pictures\\Screenshots\\Screenshot 2025-06-29 165122.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  
sobel_combined = cv2.magnitude(sobel_x, sobel_y)
sobel_combined = cv2.convertScaleAbs(sobel_combined)
cv2.imshow("Original Image", image)
cv2.imshow("Sobel - X Direction", cv2.convertScaleAbs(sobel_x))
cv2.imshow("Sobel - Y Direction", cv2.convertScaleAbs(sobel_y))
cv2.imshow("Sobel - Combined", sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
