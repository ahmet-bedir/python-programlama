import sqlite3, os

# dosya = 'kitaplar.sqlite'
# dosya_mevcutmu = os.path.exists(dosya)
# print(dosya_mevcutmu)

with sqlite3.connect("kitaplar.sqlite") as vt:
    im = vt.cursor()

    sql = "SELECT * FROM kitaplar"
    im.execute(sql)
    veriler = im.fetchall()
    print('+' + '-'*3 + '+' + '-'*50 + '+' + '-'*50 + '+' + '-'*50 + '+')
    print("|{:<3}|{:^50}|{:^50}|{:^50}|".format("No", "Kitap Adı", "Yazar", "Fiyat"))
    print('+' + '-'*3 + '+' + '-'*50 + '+' + '-'*50 + '+' + '-'*50 + '+')
    i = 0
    for satir in veriler:
        i += 1
        print("|{:<3}|{:<50}|{:<50}|{:<50}|".format(i, satir[0], satir[1], satir[2]))
    print('+' + '-'*3 + '+' + '-'*50 + '+' + '-'*50 + '+' + '-'*50 + '+')
