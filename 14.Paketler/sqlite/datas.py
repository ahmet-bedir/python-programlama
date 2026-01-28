import sqlite3

with sqlite3.connect("kitaplar.sqlite") as vt:
    im = vt.cursor()

    sql = "SELECT * FROM kitaplar"
    im.execute(sql)
    veriler = im.fetchall()
    print('-'*154)
    print("|{:^50}|{:^50}|{:^50}|".format("Kitap Adı", "Yazar", "Fiyat"))
    print('-'*154)
    for satir in veriler:
        print("|{:<50}|{:<50}|{:<50}|".format(satir[0], satir[1], satir[2]))
    print('-'*154)
