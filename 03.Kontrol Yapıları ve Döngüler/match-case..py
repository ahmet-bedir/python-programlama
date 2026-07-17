komut = "start"

match komut:
    case "start":
        print("Sistem başlatılıyor...")
    case "stop":
        print("Sistem durduruluyor...")
    case "restart":
        print("Sistem yeniden başlatılıyor...")
    case _:
        print(f"Bilinmeyen komut: {komut}")


###
gun = "salı"

match gun:
    case "pazartesi" | "salı" | "çarşamba" | "perşembe" | "cuma":
        print("İş günü")
    case "cumartesi" | "pazar":
        print("Hafta sonu!")
    case _:
        print("Gün değil!")


# Tuple pattern matching
nokta = (3, 0)

match nokta:
    case (0, 0):
        print("Orijin noktası")
    case (x, 0):
        print(f"X ekseninde, x={x}")
    case (0, y):
        print(f"Y ekseninde, y={y}")
    case (x, y):
        print(f"Genel nokta: ({x}, {y})")