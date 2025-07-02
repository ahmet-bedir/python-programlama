# "r": (Read) okuma. Dosya konumda yoksa hata verir.
# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Dosya mevcut ise dosyayı siler ve yeniden oluşturur. 
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# "r+": Hem okuma hem yazma modunda açılır. Dosya konumda yoksa hata verir.

with open("dosya.txt","r+", encoding="utf-8") as file:
    #file.seek(20)
    print(file.read())
    file.write("yeni satır.\n")