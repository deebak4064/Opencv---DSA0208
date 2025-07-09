import cv2
image = cv2.imread("C:\\Users\\shanm\\Pictures\\Screenshots\\Screenshot 2025-06-24 142941.png")
small_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
large_image = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Original Image", image)
cv2.imshow("Smaller Image", small_image)
cv2.imshow("Larger Image", large_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
