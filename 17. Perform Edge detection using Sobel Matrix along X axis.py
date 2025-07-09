import cv2
image = cv2.imread("C:\\Users\\shanm\\Pictures\\Screenshots\\Screenshot 2025-06-29 165122.png")
watermarked = image.copy()
cv2.putText(watermarked, "DHARSHINI", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 
            1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow("Watermarked Image", watermarked)
cv2.waitKey(0)
cv2.destroyAllWindows()


