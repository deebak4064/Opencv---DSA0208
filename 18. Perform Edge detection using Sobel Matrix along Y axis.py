import cv2
image = cv2.imread("C:\\Users\\shanm\\Pictures\\Screenshots\\Screenshot 2025-06-24 143240.png")
roi = image[100:165, 150:250]
image[0:65, 0:100] = roi
cv2.imshow("Original with ROI Pasted", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
