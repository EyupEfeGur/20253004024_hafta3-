# Kapsam (Scope) ve Değişken Görünürlüğü

**Ad:** Eyüp Efe  
**Soyad:** GÜR  
**Numara:** 20253004024  
**Bölüm:** Bilişim Sistemleri ve Teknolojileri  
**GitHub Deposu:** https://github.com/EyupEfeGur/20253004024_hafta3-  

---

Python'da değişkenlerin aranma sırası **LEGB** kuralına dayanır:
- **L (Local):** Fonksiyonun kendi içi (yerel)
- **E (Enclosing):** Varsa kapsayıcı dış fonksiyon (iç içe fonksiyonlarda)
- **G (Global):** Dosya/modül geneli
- **B (Built-in):** Python'ın kendi hazır fonksiyon ve adları (`len`, `print` vb.)

---

## Örnek 1: Global Değişkeni Okuma

```python
x = 10

def oku():
    print(x)

oku()
```

- **Tahmin:** 10
- **Gerçek Sonuç:** 10
- **Açıklama:**  
  `oku()` fonksiyonunun içinde `x` adında yerel bir değişken tanımlanmamış. Bu yüzden Python LEGB kuralına göre bir üst kapsama (Global) bakar ve oradaki `x = 10` değerini ekrana yazdırır.

---

## Örnek 2: Fonksiyon İçinde Yeni Değişken Tanımlama

```python
x = 10

def degistir():
    x = 20
    print("İçeride:", x)

degistir()
print("Dışarıda:", x)
```

- **Tahmin:**  
  İçeride: 20  
  Dışarıda: 10
- **Gerçek Sonuç:**  
  İçeride: 20  
  Dışarıda: 10
- **Açıklama:**  
  Fonksiyon içinde `x = 20` yazıldığında, fonksiyonun kendi yerel (local) kapsamında yeni bir `x` oluşturulur. Bu yerel değişken dışarıdaki global `x`'i etkilemez. Bu yüzden fonksiyon içinde 20 basılırken, fonksiyon bittiğinde dışarıdaki global `x` hala 10 olarak kalır.

---

## Örnek 3: Hata Durumu (UnboundLocalError)

```python
x = 10

def arttir():
    x = x + 1

arttir()
```

- **Tahmin:** Hata verir (UnboundLocalError).
- **Gerçek Sonuç:**  
  `UnboundLocalError: cannot access local variable 'x' where it is not associated with a value`
- **Açıklama:**  
  Fonksiyon gövdesinde `x = x + 1` satırında sol tarafta atama yapıldığı için Python, fonksiyon içindeki `x`'i doğrudan yerel (local) bir değişken sayar.  
  İşlem sırası sağ taraftan başladığı için `x + 1` hesaplanmak istenir fakat yerel `x`'e henüz hiçbir başlangıç değeri verilmemiştir. Python bu yüzden "yerel değişkene değer atanmadan erişilmeye çalışıldı" diyerek `UnboundLocalError` hatası fırlatır. Fonksiyon içinde atama olduğu için dışarıdaki global `x = 10` değerine hiç bakmaz.

**Nasıl Çözülür?**
- En doğru yöntem fonksiyonu saf (pure) yapıp parametre olarak alıp yeni değeri döndürmektir:
  ```python
  def arttir(deger):
      return deger + 1
  ```
- İç içe fonksiyonlarda (closure) ise üst fonksiyondaki değişkene erişmek için `nonlocal` anahtar kelimesi kullanılır.
