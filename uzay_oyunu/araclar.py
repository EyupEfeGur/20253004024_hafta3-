# Ad : Eyüp Efe
# Soyad : GÜR
# Numara : 20253004024
# Bölüm : Bilişim Sistemleri ve Teknolojileri

# Sayaç ve sıralama fonksiyonları
# Sure olcen sarmalayici fonksiyon

import time


def hamle_sayaci():
    """Her çağrıldığında 1 artıran sayaç fonksiyonu."""
    sayac = 0

    def arttir():
        nonlocal sayac
        sayac += 1
        return sayac

    return arttir


def en_bagli_gezegenler(galaksi: dict) -> list:
    """Gezegenleri bağlantı sayısına göre çoktan aza sıralar."""
    baglantilar = galaksi["baglantilar"]
    return sorted(baglantilar.keys(), key=lambda p: (-len(baglantilar[p]), p))


def sure_olc(fonksiyon):
    """Fonksiyonun çalışma süresini ölçen sarmalayıcı."""
    def sarmalayici(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"Çalışma süresi: {bitis - baslangic:.6f} saniye")
        return sonuc

    return sarmalayici


if __name__ == "__main__":
    try:
        from uzay_oyunu.galaksi import veri_yukle
    except ModuleNotFoundError:
        from galaksi import veri_yukle

    g = veri_yukle()
    print("En bağlı gezegenler:", en_bagli_gezegenler(g))

    # Süre ölçüm testi
    olculen = sure_olc(en_bagli_gezegenler)
    print("Süre ölçümlü sonuç:", olculen(g))
