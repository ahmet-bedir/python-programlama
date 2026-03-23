import mysql.connector as mysql

class Urun:
    def __init__(self):
        self.baglanti = mysql.connect(
            host = "127.0.0.1",
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
        imlec.execute(sql,degerler) #execute fonksiyonu, değer(value) olarak demet(tuple) alır.
        try:
            self.baglanti.commit()
            print(f'{imlec.rowcount} tane kayıt eklendi')
            print(f'son eklenen kaydın id: {imlec.lastrowid}')
        except mysql.Error as err:
            print('hata:', err)
        finally:
            self.baglanti.close()
            print('database bağlantısı kapandı.')

    def cokUrunEkle(self, liste):
        self.liste = liste

        imlec = self.baglanti.cursor()
        sql = """INSERT  INTO urunler (urun_adi, fiyat, url, aciklama)
        VALUES (%s,%s,%s,%s);"""
        degerler = self.liste
        imlec.executemany(sql,degerler) #executemany fonksiyonu, değer(value) olarak liste(list) alır.
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
        # liste = imlec.fetchall() #fetchall fonksiyonu, tüm kayıtları liste(list) olarak döndürür.
        # for i in liste:
        #     print(i)
        tekKayit = imlec.fetchone() #fetchone fonksiyonu, tek bir kayıt döndürür.
        print(tekKayit)

        self.baglanti.close()
###
# nesneUrunEkle = Urun()
# nesneUrunEkle.urunEkle("samsung s8",9000,"s8.jpg","akıllı telefon")

###
# liste = [
# ('Android Tv',20000,'and.png','hd'),
# ('Elektirikli Süpürge',15000,'supurge.jpeg','sil süpür'),
# ('Lc Tv',20000,'lcd.png','full hd'),
# ('Çalı Süpürge',15000,'cali.jpeg','sil süpür'),
# ]
# nesneCokUrunEkle = Urun()
# nesneCokUrunEkle.cokUrunEkle(liste)

###
nesneUrunleriListele = Urun()
nesneUrunleriListele.urunListesi()
