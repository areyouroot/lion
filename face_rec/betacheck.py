# this checks the mesure ment avalible in the data base then prints all the details of the
#  user and does the photo does exists or not

import cv2
import numpy as np
import face_recognition as fc
import os
import sqlite3

conn = sqlite3.connect('face.db',isolation_level=None)
c = conn.cursor()
c.execute("""
CREATE TABLE face (pic BLOB)
""")

def read_img():

    path = 'test'
    images = []
    classnames = []
    mylist = os.listdir(path)
    print(mylist)

    for cls in mylist:
        curimg=cv2.imread(f'{path}/{cls}')
        images.append(curimg) #ADDS ALL image in the specified folder 
        classnames.append(os.path.splitext(cls)[0]) # removes the extension

    print (classnames)
    findEncodings(images)

read_img()


'''
import sqlite3 as sql
import numpy as np
import json
con = sql.connect('test.db',isolation_level=None)
cur = con.cursor()
cur.execute("DROP TABLE FOOBAR")
cur.execute("CREATE TABLE foobar (id INTEGER PRIMARY KEY, array BLOB)")
cur.execute("INSERT INTO foobar VALUES (?,?)", (None, json.dumps(np.arange(0,500,0.5).tolist())))
con.commit()
cur.execute("SELECT * FROM FOOBAR")
data = cur.fetchall()
print data
data = cur.fetchall()
my_list = json.loads(data[0][1])
'''