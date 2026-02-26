import mysql.connector as mysql

class Urun:
    def __init__(self):
        self.baglanti = mysql.connect(
            host = "127.0.0.1", # 192.23.45.56
            user = "ahmet",
            password = "a",
            database = "db"
        )
    def urunEkle(self, urun_adi, fiyat, url, aciklama):
        self.urun_adi = urun_adi
        self.fiyat = fiyat
        self.url = url
        self.aciklama = aciklama

        imlec = self.baglanti.cursor()
        sql = """INSERT INTO urunler (urun_adi, fiyat, url, aciklama)
        VALUES (%s,%s,%s,%s);"""
        degerler = (self.urun_adi, self.fiyat, self.url, self.aciklama)
        imlec.execute(sql,degerler)
        try:
            self.baglanti.commit()
            print(f'{imlec.rowcount} tane kayıt eklendi')
            print(f'son eklenen kaydın id: {imlec.lastrowid}')
        except mysql.Error as err:
            print('hata:', err)
        finally:
            self.baglanti.close()
            print('database bağlantısı kapandı.')

    def urunListesi(self):
        imlec = self.baglanti.cursor()
        sql = """SELECT * FROM urunler;"""
        imlec.execute(sql)
        liste = imlec.fetchall()
        for i in liste:
            print(i)
        self.baglanti.close()

u1 = Urun()
u1.urunListesi()

# u1.urunEkle("samsung s7",5000,"s7.jpg","akıllı telefon")
