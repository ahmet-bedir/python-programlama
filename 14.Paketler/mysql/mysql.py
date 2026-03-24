import mysql.connector as mysql

class Urun:
    def __init__(self):
        self.baglanti = mysql.connect(
            host = "127.0.0.1",
            user = "ahmet",
            password = "a",
            database = "db")
        
    ###
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
            
    ###
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
            
    ###
    def urunListesi(self):
        imlec = self.baglanti.cursor()
        sql = """SELECT * FROM urunler;""" #Tüm kayıtları çekmek istediğimiz için * kullanırız.
        sql = """SELECT * FROM urunler ORDER BY urun_adi DESC;""" #urun_adi'na göre azalan sırada sıralamak istediğimiz için ORDER BY kullanırız. Ve DESC ile azalan sırada sıralarız. Eğer artan sırada sıralamak istiyorsak ASC kullanırız.
        imlec.execute(sql)
        try:
            liste = imlec.fetchall() #fetchall fonksiyonu, tüm kayıtları liste(list) olarak döndürür.
            for i in liste:
                print(i)
                
            # tekKayit = imlec.fetchone() #fetchone fonksiyonu, tek bir kayıt döndürür. Eğer birden fazla kayıt varsa, ilk kaydı döndürür. Eğer hiç kayıt yoksa, None döndürür.
            # print(tekKayit)
        except mysql.Error as err:
            print('hata:', err)
        finally:
            self.baglanti.close()
            
    ###
    def urunId(self, id):
        imlec = self.baglanti.cursor()
        sql = """Select * From urunler Where id=%s""" #id'ye göre kayıt çekmek istediğimiz için, id'yi parametre olarak alırız. Ve sql sorgusunda %s ile id'yi belirtiriz.
        urunId = (id,) #id'yi demet(tuple) olarak tanımlarız. Çünkü execute fonksiyonu, değer(value) olarak demet(tuple) alır.
        imlec.execute(sql,urunId)
        sonuc = imlec.fetchone()
        print(f'id: {sonuc[0]}\nÜrün adı: {sonuc[1]}\nFiyat: {sonuc[2]}')
        self.baglanti.close()
        
    ###
    def urunBilgisi(self):
        imlec = self.baglanti.cursor()

        sql = """SELECT COUNT(*) FROM urunler;""" #urunler tablosundaki kayıt sayısını çekmek istediğimiz için COUNT(*) kullanırız.
        sql = """SELECT AVG(fiyat) FROM urunler;""" #urunler tablosundaki fiyat ortalamasını çekmek istediğimiz için AVG() kullanırız.
        sql = """SELECT SUM(fiyat) FROM urunler;""" #urunler tablosundaki fiyat toplamını çekmek istediğimiz için SUM() kullanırız.
        sql = """SELECT MIN(fiyat) FROM urunler;""" #urunler tablosundaki en düşük fiyatı çekmek istediğimiz için MIN() kullanırız.
        sql = """SELECT MAX(fiyat) FROM urunler;""" #urunler tablosundaki en yüksek fiyatı çekmek istediğimiz için MAX() kullanırız.
        sql = """SELECT urun_adi,fiyat FROM urunler WHERE fiyat = (SELECT MAX(fiyat) FROM urunler);""" #urunler tablosundaki en yüksek fiyata sahip ürünleri çekmek istediğimiz için bu sorguyu kullanırız.

        imlec.execute(sql)

        sonuc = imlec.fetchone()    

        print(f'En Pahalı Ürün: {sonuc[0]} - Fiyat: {sonuc[1]}')
        self.baglanti.close()

        
###
# nesneUrunEkle = Urun()
# nesneUrunEkle.urunEkle("dell laptop",21000,"dell.jpg","dizüstü bilgisayar")

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

###
nesneUrunId = Urun()
nesneUrunId.urunId(13)

###
nesneUrunBilgisi = Urun()
nesneUrunBilgisi.urunBilgisi()
