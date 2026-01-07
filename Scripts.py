import cv2

init = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
imagem = cv2.imread('dataset/img.png')

imagemTransmuted = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = init.detectMultiScale(imagemTransmuted, scaleFactor=1.1, minNeighbors=3, minSize=(20,30))


print(faces)

for(x,y,w,h) in faces:
    cv2.rectangle(imagem,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("faces", imagem)
cv2.waitKey()