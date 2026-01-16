import cv2

eye = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")
face = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

imagem = cv2.imread('dataset/img.png')

imagemTransmuted = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = face.detectMultiScale(imagemTransmuted)


for(x,y,w,h) in faces:
    leitura = cv2.rectangle(imagem,(x,y),(x+w,y+h),(0,255,0),2)
    localEye = imagem[y:y +h, x:x +w]
    localEyeGray= cv2.cvtColor(localEye, cv2.COLOR_BGR2GRAY)
    eyes = eye.detectMultiScale(localEyeGray)

    for ox, oy, ow, oh in eyes:
        cv2.rectangle(localEye, (ox, oy), (ox+ow, oy+oh), (0,255,0), 2)


cv2.imshow("detecta", imagem)
cv2.waitKey()