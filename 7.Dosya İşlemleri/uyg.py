"""
dosya = open("metin.txt","w",encoding="cp1254")
dosya.write("ağaç\n")
dosya.seek(5)
liste = ["a\n","b\n","c\n","ç\n"]
a.writelines(liste)
a.close()
"""
# cp1254 ile kodlanmış bir belgeyi UTF-8 ile açmaya kalkışırsanız veya siz hiçbir kod çözücü belirtmediğiniz halde kullandığınız işletim sistemi öntanımlı olarak dosyaları açmak için cp1254 harici bir kod çözücüyü kullanıyorsa, dosyayı okuma esnasında 'UnicodeDecodeError' hatası alırsınız.
with open("metin.txt",encoding="utf-8") as dosya:
    print(dosya.read())