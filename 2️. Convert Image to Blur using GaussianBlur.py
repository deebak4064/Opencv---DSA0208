
import cv2


# Read your PNG image
img = cv2.imread('C:/Documents/Computer Vision/Exp 2.png')

# Safety check if image was loaded
if img is None:
    print("Error: Image not found or path is incorrect.")
else:
    blur = cv2.GaussianBlur(img, (15, 15), 0)

    cv2.imshow('Original Image', img)
    cv2.imshow('Blurred Image', blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
