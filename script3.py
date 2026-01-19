import cv2

webcam = cv2.VideoCapture(0)
classificadorFace = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
while True:
    ret, frame = webcam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = classificadorFace.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2. imshow("faces", frame)

    if cv2.waitKey(1) == ord('f'):
        break

webcam.release()
cv2.destroyAllWindows()
