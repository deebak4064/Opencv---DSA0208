import cv2

cap = cv2.VideoCapture('"C:\Documents\Computer Vision\WIN_20241118_12_23_30_Pro.mp4"')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Video', frame)
    
    # Wait 30ms for normal speed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
