x = 42
y = x

print(f"x: {x}, Tipi: {type(x)}, Bellek Adrsi: {id(x)}")
print(f"x: {x}, Tipi: {type(x)}, Bellek Adrsi: {id(y)}")
print(x is y)  # True — aynı nesne!

print('-' * 50)

x = 99

print(f"x: {x} ({id(x)})")
print(f"y: {y} ({id(y)})")  # 42 — y hâlâ eski nesneye bağlı
print(x is y)
