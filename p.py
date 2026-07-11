not_ortalamasi = 8

if not_ortalamasi >= 90:
    harf = "AA"
elif not_ortalamasi >= 80:
    harf = "BA"
elif not_ortalamasi >= 70:
    harf = "BB"
elif not_ortalamasi >= 60:
    harf = "CB"
else:
    harf = "FF"

print(f"Harf notun: {harf}")  # Harf notun: BB