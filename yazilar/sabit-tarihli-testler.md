---
baslik: Sabit tarihli testler gün değişince kırılır
tarih: 2026-10-01
ozet: Bir kota testi sabit bir tarih yazdığı için gece yarısı CI'ı kırdı. Tarihi bugüne göre hesaplamak sorunu kapattı.
etiketler: [python, test, ci]
herkese_acik: false
---
Bir kota hesaplayıcının testleri, "dün" kullanılmış olsun diye veritabanına sabit bir tarih (`2026-09-30`) yazıyordu. Kod ise kotayı **bugüne** göre sayıyordu. Test yazıldığı gün yeşildi. UTC gece yarısı geçince CI kırmızıya döndü; eski kodla bugünün tarihinde çalıştırınca da iki test gerçekten kırıldı. Sabit "dün", bir gün sonra artık "dün" değildi.

## Neden fark edilmedi

Testin başarısı takvime bağlıydı ama bu bağımlılık hiçbir yerde yazmıyordu. Sabit tarih, testi okuyana "bu sadece bir örnek değer" gibi görünüyor. Oysa kod o değeri bir *göreli aralıkla* karşılaştırıyor.

## Çözüm

Tarihi testin içinde bugüne göre türet:

```python
from datetime import datetime, timedelta, timezone

bugun = datetime.now(timezone.utc).date()
dun = bugun - timedelta(days=1)
```

Gece yarısı sınırında çalışan bir test hâlâ yarış yaşayabilir. Bunu kapatmak istiyorsan saati dışarıdan veren bir parametre (ya da sahte bir saat) kullan. Bu, kodu da test edilebilir yapar.

## Küçük bir ders daha

Sabit tarih birden çok test dosyasındaydı; uçtan uca dosyadaki üçüncü örnek yalnızca **tam test paketi** çalışınca ortaya çıktı. Tek bir dosyayı çalıştırıp commit atmak yetmez. Paketi sonuna kadar bekle.

Bu yüzden CI'a küçük bir adım eklemek mantıklı: testlerde `20\d\d-\d\d-\d\d` biçiminde sabit tarih arayan ve bulduklarını listeleyen bir betik. Yanlış pozitifleri olur (gerçekten sabit olması gereken tarihler), ama "bunu bilerek yazdım" diye işaretlenebilir.
