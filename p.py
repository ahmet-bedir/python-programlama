def bilgi_goster(ad, yas, sehir):
    print(f"{ad}, {yas} yaşında, {sehir}'da yaşıyor.")

# Keyword: sıra önemli değil!
bilgi_goster(yas=25, sehir="İstanbul", ad="Ahmet")
# Ahmet, 25 yaşında, İstanbul'da yaşıyor. ✅

# İkisini karıştırabilirsin (ama positional önce gelmeli)
bilgi_goster("Ahmet", 6, sehir="izmr")
# Ahmet, 25 yaşında, İstanbul'da yaşıyor. ✅