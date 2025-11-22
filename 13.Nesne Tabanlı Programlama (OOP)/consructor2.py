import consructor as con

print(dir(con))

ahmet = con.Calisan()
ahmet.kabiliyetleri.append("net")
print(ahmet.kabiliyetleri)

mehmet = con.Calisan()
print(mehmet.kabiliyetleri)