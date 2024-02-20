import cv2

# Detect faces from a video
#load some pre-trained data on face frontals from opencv (hear cascade algorithm)
trained_face_data = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")

# Capture video from webcam
webcam = cv2.VideoCapture("media/video.mp4")

# Iterate forever over frames
while True:
    # Read the current frame
    successful_frame_read, frame = webcam.read()

    # Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img, scaleFactor=1.6, minNeighbors=5)

    # Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Displays the image
    cv2.imshow("Faybian Byrd Face Detector", frame)

    # Waits until a key is pressed before closing the image
    key = cv2.waitKey(1)

    # Stop if Q key is pressed
    if key==81 or key==113:
        break

# Release the VideoCapture object
webcam.release()

print("Code Completed")