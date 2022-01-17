#get all the inputs from the user asks for a photo then if data base is not avalible then creates it 
#else updates in the existing data base

import sqlite3
from tkinter import PhotoImage



con = sqlite3.connect('face.db')
c = con.cursor()

#c.execute("CREATE TABLE face (id INTEGER PRIMARY KEY,pic BLOOB)") #un comment it if the data base is not avalible

#get id and photo to insert

c.execute("SELECT id FROM face")
print(c.fetchall())
con.commit()
con.close()

