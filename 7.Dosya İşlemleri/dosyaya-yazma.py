#    "w" : (Write) yazma modu. 
#    ** Dosya konumda yoksa, oluşturur. 
#    ** Eğer konumda aynı dosya varsa dosyayı siler ve yeni oluşturur.

with open("dosya.txt","w",encoding="utf-8") as file:
    file.write("Eren Kozlu\n")
    file.write("Fatih Gün\n")

with open("dosya.txt","r",encoding="utf-8") as file:
    print(file.read())