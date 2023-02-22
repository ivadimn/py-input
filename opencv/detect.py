import cv2
import sys

#image_path = sys.argv[1]
#casc_path = sys.argv[1]

image_path = "face01.jpg"
casc_path = "haarcascade.xml"

face_cascade = cv2.CascadeClassifier(casc_path)

image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)
print("Found {0} faces".format(len(faces)))
