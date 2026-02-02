import sqlite3, os

with sqlite3.connect("db.sqlite") as vt:
    im = vt.cursor()

    sql = "SELECT * FROM personel"
    im.execute(sql)
    veriler = im.fetchall()



    dolgu = 10

    for satir in veriler:
        if len(satir[0]) > dolgu:
            dolgu = len(satir[0])
        elif len(satir[1]) > dolgu:
            dolgu = len(satir[1])
        elif len(satir[2]) > dolgu:
            dolgu = len(satir[2])

    i = 0
    print('+' + '-'*dolgu + '+' + '-'*dolgu + '+' + '-'*dolgu + '+')
    print("|{:^10}|{:^10}|{:^10}|".format("İsim", "Soyisim", "Memleket"))
    print('+' + '-'*dolgu + '+' + '-'*dolgu + '+' + '-'*dolgu + '+')

    for satir in veriler:
        i += 1
        print("|{:<10}|{:<10}|{:<10}|".format(satir[0], satir[1], satir[2]))
        print('+' + '-'*dolgu + '+' + '-'*dolgu + '+' + '-'*dolgu + '+')

    print(f"Toplam {i} Kayıt.")
