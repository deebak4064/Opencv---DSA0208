import cv2

# Load the image
img = cv2.imread('Exp 1.png')

if img is None:
    print("Error: Image not found.")
else:
    # Resize to bigger size (double)
    bigger = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    # Resize to smaller size (half)
    smaller = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # Show images
    cv2.imshow('Original Image', img)
    cv2.imshow('Bigger Image', bigger)
    cv2.imshow('Smaller Image', smaller)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
