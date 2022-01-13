from PIL.Image import Image
import cv2
import numpy as np
import face_recognition as fc
import os

path = 'images'
images = []
classnames = []
mylist = os.listdir(path)
print(mylist)

for cls in mylist:
    curimg=cv2.imread(f'{path}/{cls}')
    images.append(curimg)
    classnames.append(os.path.splitext(cls)[0])
print (classnames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = fc.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodelistknown = findEncodings(images)
print ("encodeding complete")

cap = cv2.VideoCapture(0)

while True:
    sucess,img = cap.read()
    imgs = cv2.resize(img,(0,0),None,0.25,0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

    facescurframe = fc.face_locations(imgs)
    encodescurframe = fc.face_encodings(imgs,facescurframe)

    for encodefaces,faceloc in zip(encodescurframe,facescurframe):
        matches = fc.compare_faces(encodelistknown,encodefaces)
        facedis = fc.face_distance(encodelistknown,encodefaces)
        print(facedis)
        matchindex = np.argmin(facedis)

        if matches[matchindex]:
            name = classnames[matchindex].upper()
            print(name)
            y1,x2,y2,x1 = faceloc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,225,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,225,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

    cv2.imshow('webcam',img)
    cv2.waitKey(1)

