#get all the inputs from the user asks for a photo then if data base is not avalible then creates it 
#else updates in the existing data base

import sqlite3
from tkinter import PhotoImage



con = sqlite3.connect('db.sqlite3')
c = con.cursor()

#c.execute("CREATE TABLE face (id INTEGER PRIMARY KEY,pic BLOOB)") #un comment it if the data base is not avalible

#get id and photo to insert

c.execute("SELECT name FROM sqlite_schema WHERE type = 'table' AND name NOT LIKE 'sqlite_%'")
print(c.fetchall())
c.execute("SELECT * FROM lion_profile")
print(c.fetchall())
print("________________________________________________________________________________________")
c.execute("SELECT * FROM auth_user")
print(c.fetchall())
con.commit()
con.close()

