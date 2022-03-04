#get all the inputs from the user asks for a photo then if data base is not avalible then creates it 
#else updates in the existing data base

import sqlite3
from tkinter import PhotoImage


id = int(input("enter the employee id: "))
con = sqlite3.connect('face.db')
c = con.cursor()

c.execute("CREATE TABLE face (id INTEGER PRIMARY KEY,pic BLOOB)") #un comment it if the data base is not avalible

#get id and photo to insert

with open('./test/elone.jpg','rb') as photo: #reads image and stores into a variable
    img = photo.read()
    
c.execute("""
INSERT INTO face (id, pic) VALUES (?,?)
""",(id, img))

c.execute("SELECT * FROM face")
print(c.fetchall())
con.commit()
con.close()

