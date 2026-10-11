# Ad : Eyüp Efe
# Soyad : GÜR
# Numara : 20253004024
# Bölüm : Bilişim Sistemleri ve Teknolojileri

# Fonksiyonların birim testleri

import pytest
from uzay_oyunu.oyun import envanter_metni, hedef_menusu


def test_envanter_metni_dolu():
    """Eşyalar varken doğru metin dönmeli."""
    sonuc = envanter_metni(True, False, True)
    assert sonuc == "Sende: bol kredi, yetenekli bir pilot"


def test_envanter_metni_bos():
    """Eşya yoksa boş metin dönmeli."""
    assert envanter_metni(False, False, False) == ""


def test_envanter_metni_tum_esyalar():
    """Tüm eşyalar varken tam liste dönmeli."""
    sonuc = envanter_metni(True, True, True)
    assert sonuc == "Sende: bol kredi, hiper motor, yetenekli bir pilot"


def test_hedef_menusu():
    """Hedefler numaralı liste şeklinde dönmeli."""
    beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(["centauri", "sirius"]) == beklenen


def test_hedef_menusu_tek_hedef():
    """Tek hedef olduğunda doğru dönmeli."""
    beklenen = "Nereye gitmek istersin?\n[1] orion"
    assert hedef_menusu(["orion"]) == beklenen

def test_gorev_kaydi(capsys):
    """Standart parametrelerle çağrıyı test ediyoruz."""
    from uzay_oyunu.kayit import gorev_kaydi

    gorev_kaydi("Kara deliğe atla", "Kredi kazan", "Pilot bul", "Hiperdrive al", oncelik="yüksek", sorumlu="Ayşe")
    captured = capsys.readouterr()
    beklenen = (
        "[YÜKSEK] Kara deliğe atla\n"
        " 1. Kredi kazan\n"
        " 2. Pilot bul\n"
        " 3. Hiperdrive al\n"
        " sorumlu: Ayşe\n"
    )
    assert captured.out == beklenen


def test_gorev_kaydi_unpacking(capsys):
    """* ve ** ile açarak çağırmayı test ediyoruz."""
    from uzay_oyunu.kayit import gorev_kaydi

    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"sorumlu": "Ayşe"}
    gorev_kaydi("Kara deliğe atla", *adimlar, oncelik="yüksek", **ekler)
    captured = capsys.readouterr()
    beklenen = (
        "[YÜKSEK] Kara deliğe atla\n"
        " 1. Kredi kazan\n"
        " 2. Pilot bul\n"
        " 3. Hiperdrive al\n"
        " sorumlu: Ayşe\n"
    )
    assert captured.out == beklenen

def test_galaksi_kur_varsayilan_yakit():
    """Yakıt verilmediğinde 50 olmalı."""
    from uzay_oyunu.galaksi import galaksi_kur

    g = galaksi_kur(["mars"], {"mars": []}, "mars")
    assert g["konum"] == "mars"
    assert g["yakit"] == 50


def test_galaksi_kur_gecersiz_baslangic():
    """Geçersiz başlangıçta ValueError vermeli."""
    from uzay_oyunu.galaksi import galaksi_kur

    with pytest.raises(ValueError):
        galaksi_kur(["mars"], {"mars": []}, "dünya")


def test_veri_yukle():
    """JSON'dan doğru verilerin yüklendiğini kontrol ediyoruz."""
    from uzay_oyunu.galaksi import veri_yukle

    g = veri_yukle()
    assert g["konum"] == "dünya"
    assert g["yakit"] == 100
    assert "sirius" in g["baglantilar"]
    assert g["baglantilar"]["dünya"] == ["centauri", "sirius"]
