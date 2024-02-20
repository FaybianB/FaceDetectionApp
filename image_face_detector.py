import cv2

# Detect faces for an image
#load some pre-trained data on face frontals from opencv (hear cascade algorithm)
trained_face_data = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")

# Choose an image to detect faces in
img = cv2.imread("media/frontal.png")

# Must convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img, scaleFactor=1.15, minNeighbors=5)

# Draw rectangles around the faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Displays the image
cv2.imshow("Faybian Byrd Face Detector", img)

# Waits until a key is pressed before closing the image
cv2.waitKey()

print("Code Completed")