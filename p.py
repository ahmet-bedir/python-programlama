# İlk ve son elemanı ayır, gerisini topla
ilk, *orta, son = [1, 2, 3, 4, 5]
print(ilk)   # 1
print(orta)  # [2, 3, 4]
print(son)   # 5

# Sadece ilk elemanı al, gerisini yoksay
bas, *_ = "Python".split()
# _ yaygın olarak "umursamıyorum" anlamında kullanılır
print(bas)
