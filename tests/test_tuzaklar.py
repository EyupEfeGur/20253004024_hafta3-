# Ad : Eyüp Efe
# Soyad : GÜR
# Numara : 20253004024
# Bölüm : Bilişim Sistemleri ve Teknolojileri

# Varsayilan arguman tuzagi ve None kalibi

import pytest


def yakit_ekle(miktar: int, depo=None) -> list:
    """Depoya yakıt ekler, varsayılan liste tuzağını önlemek için None kullanılır."""
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


def test_yakit_ekle_tuzak():
    """Boş bırakıldığında her çağrıda bağımsız yeni liste oluşmalı."""
    gemi1 = yakit_ekle(50)
    assert gemi1 == [50]

    gemi2 = yakit_ekle(30)
    assert gemi2 == [30]


def test_yakit_ekle_mevcut_depo():
    """Var olan bir depo verildiğinde üstüne ekleme yapmalı."""
    ozel_depo = [10, 20]
    sonuc = yakit_ekle(30, ozel_depo)
    assert sonuc == [10, 20, 30]
    assert sonuc is ozel_depo
