import cv2

# Read the image
image = cv2.imread('C:/Users/dilli/OneDrive/Documents/Computer Vision/Exp 1.png')  # Replace with your image filename

# Show the original image
cv2.imshow('Original Image', image)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Show the grayscale image
cv2.imshow('Grayscale Image', gray_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
