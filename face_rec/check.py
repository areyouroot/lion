# imports

import sqlite3
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
encode = fc.face_encodings(img)[0]
print(encode)
