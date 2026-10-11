# Ad : Eyüp Efe
# Soyad : GÜR
# Numara : 20253004024
# Bölüm : Bilişim Sistemleri ve Teknolojileri

# Uzay oyunu seyahat başlangıç fonksiyonu


def travel() -> None:
    print("Sende: bol kredi, yetenekli bir pilot")
    planet = "dünya"
    yakit = 100

    while True:
        if planet == "dünya":
            destinations = ["centauri", "sirius"]
        elif planet == "centauri":
            destinations = ["sirius", "dünya", "orion"]
        elif planet == "sirius":
            destinations = ["centauri", "dünya", "orion", "kara_delik"]
        elif planet == "orion":
            destinations = ["kara_delik", "sirius"]
        elif planet == "kara_delik":
            destinations = []
        else:
            destinations = []

        if not destinations:
            print("Kara deliğe ulaştın veya yol bitti!")
            break

        print(f"\nŞu anki konum: {planet}")
        print("Nereye gitmek istersin?")
        for i, h in enumerate(destinations, 1):
            print(f"[{i}] {h}")

        secim = input("Seçiminiz (Çıkış için q): ")
        if secim.lower() == "q":
            break

        try:
            index = int(secim) - 1
            if 0 <= index < len(destinations):
                planet = destinations[index]
                yakit -= 10
            else:
                print("Geçersiz seçim!")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")


if __name__ == "__main__":
    travel()
