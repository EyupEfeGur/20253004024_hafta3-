# Ad : Eyüp Efe
# Soyad : GÜR
# Numara : 20253004024
# Bölüm : Bilişim Sistemleri ve Teknolojileri

# Esnek parametreler ve gorev kaydi


def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler) -> None:
    """Görev adımlarını ve ek bilgileri ekrana yazdırır."""
    print(f"[{oncelik.upper()}] {baslik}")

    for i, adim in enumerate(adimlar, 1):
        print(f" {i}. {adim}")

    for anahtar, deger in ekler.items():
        print(f" {anahtar}: {deger}")


if __name__ == "__main__":
    # 1. Çağrı: argümanları tek tek vererek çağırma
    gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik="yüksek",
        sorumlu="Ayşe",
    )

    # 2. Çağrı: listeyi * ve sözlüğü ** ile açarak çağırma
    adimlar_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_bilgiler = {"sorumlu": "Ayşe"}
    gorev_kaydi(
        "Kara deliğe atla",
        *adimlar_listesi,
        oncelik="yüksek",
        **ek_bilgiler,
    )
