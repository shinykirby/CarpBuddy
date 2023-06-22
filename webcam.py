import cv2

cap = cv2.VideoCapture(0)  # 0 is the ID of the first webcam

while True:
    ret, frame = cap.read()  # Capture a frame
    if not ret:
        break

    # Process the frame here...

    cv2.imshow('Webcam', frame)  # Display the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Quit if 'q' is pressed
        break

cap.release()  # Release the webcam
cv2.destroyAllWindows()  # Close the window
