import sqlite3 as sql
import numpy as np
import json
con = sql.connect('test.db',isolation_level=None)
cur = con.cursor()
cur.execute("CREATE TABLE foobar (id INTEGER PRIMARY KEY, array BLOB)")
cur.execute("INSERT INTO foobar VALUES (?,?)", (None, json.dumps(np.arange(0,500,0.5).tolist())))
con.commit()
cur.execute("SELECT * FROM FOOBAR")
data = cur.fetchall()
print (data)