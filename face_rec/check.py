# imports

import sqlite3
from sre_constants import SUCCESS
from tabnanny import check
import cv2
import numpy as np
import face_recognition as fc
import os

#code
id = str(input("enter your id: "))
con = sqlite3.connect('face.db')
c = con.cursor()
print(id)
c.execute("SELECT pic FROM face WHERE id = '%s'" % (id))
img = (c.fetchall()[0][0])

with open("check.jpg","wb") as file:
    file.write(img)

cwd = os.getcwd()
img = cv2.imread(f'{cwd}/check.jpg')
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
facescurframe = fc.face_locations(img)
encode = fc.face_encodings(img,facescurframe)
print(encode)

cap = cv2.VideoCapture(0)
while True:
    SUCESS,img = cap.read()
    imgs = cv2.resize(img,(0,0),None,0.25,0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

    facescurframe = fc.face_locations(img)
    encode2=fc.face_encodings(img,facescurframe)
    for encodeface,faceloc in zip(encode2,facescurframe):
        match = fc.compare_faces(encode,encodeface)
    #'''Returns a single iterator object, 
    #    having mapped values from all the containers.'''
        
    print (match)