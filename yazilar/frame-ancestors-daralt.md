---
baslik: Bir aracı iframe'e alırken frame-ancestors'ı kaldırma, daralt
tarih: 2026-10-01
ozet: Küçük web araçlarını tek bir panelde sekme olarak göstermek için başlığı silmek kolay ama güvensiz. Başlığı tek bir origin'e daraltmak ve girdiyi sıkı doğrulamak daha doğru.
etiketler: [güvenlik, csp, web]
herkese_acik: false
---
Yerel olarak çalışan birkaç küçük aracı tek bir panelde sekme olarak göstermek istedim. Her araç, kendi yanıtlarında `Content-Security-Policy: frame-ancestors 'none'` gönderiyordu: yani hiçbir sayfa onu `<iframe>` içine alamaz. Panelde göstermek için en kısa yol bu başlığı silmekti. Yapmadım.

## Neden silmedim

`frame-ancestors`, tıklama kaçırma (clickjacking) saldırısına karşı savunmadır. Başlığı kaldırmak, o aracı **herhangi** bir sitenin iframe'ine açık bırakır. Bu araçlar yerelde çalışsa bile tarayıcı, kötü niyetli bir sayfanın `localhost` üzerindeki aracı çerçeveleyip kullanıcıyı tıklamaya yönlendirmesine izin verir.

## Ne yaptım

Varsayılan hâlâ `'none'`. Panelin origin'i ortam değişkeniyle verilirse başlık yalnızca o origin'e izin verecek şekilde daralıyor:

```
frame-ancestors 'none'                      # değişken yok
frame-ancestors https://panel.example       # değişken var
```

Değişken belirtilmemişse davranış öncekiyle aynı. Yani bu değişiklik izin verici bir varsayılan getirmiyor, yalnızca açıkça yapılandırılmış tek bir origin'i açıyor.

## Girdiyi doğrularken tuzak: `$`

Origin değeri başlığa yazıldığı için biçimi sıkı doğrulamak gerekiyor; yoksa değişkene bir satır sonu koyan biri başlığa istediği direktifi ekleyebilir. İlk denemem `re.match(r"^https?://[a-z0-9.-]+(:\d+)?$", deger)` idi. Python'da `$`, dizenin **sonundan önceki satır sonunda da** eşleşir; yani `"https://panel.example\n"` bu desenden geçer.

Doğrusu `fullmatch` kullanmak (ya da `\Z`):

```python
import re

ORIGIN = re.compile(r"https?://[a-z0-9.-]+(?::\d+)?")

def gecerli_origin(deger: str) -> bool:
    return ORIGIN.fullmatch(deger) is not None
```

Genel kural: bir değeri başka bir metne gömeceksen, "tamamı bu desene uymalı" demek için `fullmatch` kullan ve `^...$` ikilisine güvenme.
