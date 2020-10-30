import cv2

#cascade dosyasını yükleme

face_cascade = cv2.CascadeClassifier('face.xml')

#resmi okuma

img = cv2.imread('indir(2).jpg')

#resmi griye çevirme

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#yüz tanıma

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

#yüzün çevresinde dikdörtgen çizme

for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
#çıktıyı göstermek
cv2.imshow('img',img)
cv2.waitKey()