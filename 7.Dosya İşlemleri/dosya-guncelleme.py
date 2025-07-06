# "a": (Append) ekleme. Dosya konumda yoksa oluşturur. Varsa dosyaya ekleme yapar.
# "r": (Read) okuma. Dosya konumda yoksa hata verir.
# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Dosya mevcut ise dosyayı siler ve yeniden oluşturur. 
# "r+": Hem okuma hem yazma modunda açılır. Dosya konumda yoksa hata verir.

#Dosyaların Sonunda Değişiklik Yapmak
with open("markalar.txt","a") as file:
    file.write("6.Bmw\n")


#Dosyaların Başında Değişiklik Yapmak
with open("markalar.txt","r+", encoding="utf-8") as file:
     markalar = file.read()
     print(markalar)
     
     input("Dosyaya ekleme yapmak için herhangi bir tuşa basınız.")
     
     markalar = "1.Toyota\n" + markalar
     file.seek(0)
     file.write(markalar)
     
     print(markalar)






with open("markalar.txt","r+",encoding="utf-8") as file: #dosyanın ortasına ekleme yapar.
    markalar = file.readlines()
    markalar.insert(2, "3-Renault\n")
    file.seek(0)
    for marka in markalar:
        file.write(marka)
    # file.writelines(markalar)


with open("markalar.txt", "r", encoding="utf-8") as file:
    print(file.read())