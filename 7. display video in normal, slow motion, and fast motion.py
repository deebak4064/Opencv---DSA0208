import cv2

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open webcam.")
else:
    print("Press 's' for slow motion, 'f' for fast motion, 'q' to quit.")

    delay = 30  # normal speed

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Webcam Video', frame)

        key = cv2.waitKey(delay) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            delay = 100  # slow motion (100 ms delay)
        elif key == ord('f'):
            delay = 1    # fast motion (1 ms delay)

    cap.release()
    cv2.destroyAllWindows()
