#code to detect face in an image
import cv2
#contain face features
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#for reading the image
img = cv2.imread("IMG_20201211_175249.jpg")
#convertng the image into gray scale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#search the coordianates of the face
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for x,y,w,h in faces:
    #method to create a  rectangular face box
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
cv2.imshow("img", img)
cv2.waitKey()
