# Pratik: Kullanıcı girdisi doğrulama
gecerli_secenekler = ["EVET", "HAYIR", "E", "H"]

cevap = input("Devam? (evet/hayır): ").upper().strip()
if cevap in gecerli_secenekler:
    print(f"Seçiminiz: {cevap}")
else:
    print("Geçersiz seçenek!")