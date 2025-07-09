import cv2
import numpy as np
image = cv2.imread("C:\\Users\\shanm\\Pictures\\Screenshots\\Screenshot 2025-06-29 165122.png")
rows, cols = image.shape[:2]
pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.float32([[10, 100], [220, 50], [100, 250], [220, 220]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(image, matrix, (cols, rows))
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
