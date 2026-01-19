import cv2

webcam= cv2.VideoCapture(0)
classificadorOlho= cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")
classificadorFace = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

while True:
    camera, frame = webcam.read()
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detect = classificadorOlho.detectMultiScale(cinza)
    for (x,y,w,h) in detect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        pegaolho= frame[y:y+h,x:x+w]
        olhocinza= cv2.cvtColor(pegaolho, cv2.COLOR_BGR2GRAY)
        localolho= classificadorFace.detectMultiScale(olhocinza)
        for (x,y,w,h) in localolho:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("frame",frame)
    if cv2.waitKey(1)  == ord('f'):
        break


webcam.release()
cv2.destroyAllWindows()