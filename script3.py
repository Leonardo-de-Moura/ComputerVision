import cv2

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    cv2.imshow("img cam" , frame)

    if cv2.waitKey(1)  == ord('f'):
        break

webcam.release()
cv2.destroyAllWindows()
