import cv2

# Replace the path below with the actual image file path
image_path = r"C:\Users\shanm\Pictures\Screenshots\Screenshot 2025-06-29 121126.png"

# Load the image
image = cv2.imread(image_path)

# Check if the image is loaded properly
if image is None:
    print("Error: Image not found or path is incorrect!")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray_image, 100, 200)

    # Display the original and processed images
    cv2.imshow('Original Image', image)
    cv2.imshow('Canny Edge Detection', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

