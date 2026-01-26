import sqlite3

vt = sqlite3.connect('db.sqlite')

im = vt.cursor() 

print(im.execute("""SELECT * FROM personel"""))

vt.commit()


vt.close()

