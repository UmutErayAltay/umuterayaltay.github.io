---
baslik: Ajan çıktısına güvenme: bir günde yakaladığım 5 hata
tarih: 2026-10-01
ozet: Yapay zekâ ajanlarına yazdırdığım kodda tek günde beş gerçek hata buldum. Hepsini testler yakaladı, raporlar değil.
etiketler: [yapay zekâ, test, kalite]
herkese_acik: false
---
Bir gün içinde iki küçük araç yazdırdım. Mekanik işleri ücretsiz bir modele bağlı ajanlara verdim, sonuçları kendim doğruladım. Altı ajanın **altısı** zaman aşımına düştü, hiçbiri rapor yazmadı, bazıları çalışma dizinlerinde yarım betikler bıraktı. Kodun büyük kısmını sonunda kendim yazdım. Ajanın bıraktığı kodda ise beş gerçek hata çıktı. Raporlar ya yoktu ya da "tamam" diyordu; hataları test yakaladı.

## 1. Tırnaklı `visibility: "private"` atlanmıyordu

Not okuyucu, `visibility: private` işaretli notları dışarıda bırakıyordu. Değer tırnak içinde (`"private"`) yazılınca karşılaştırma tutmadı ve özel not işlenmeye devam etti. Bu bir gizlilik hatası. Düzeltme: değeri tırnaklardan arındırıp küçük harfe çevirmek, ve **tırnaklı değer için ayrı bir test** yazmak.

## 2. `finditer(metin, flags)` bayrak değildir

`re.Pattern.finditer(string, pos, endpos)` imzasında ikinci argüman **başlangıç konumudur**. Büyük/küçük harf duyarsızlığı için `re.IGNORECASE` geçmek, taramayı sessizce 2. karakterden başlatıyordu. Bayrağı `re.compile` aşamasında vermek gerekiyor.

## 3. `git log` en yeni commit'i önce verir

İlk ve son commit tarihi hesaplanırken liste "ilk eleman = en eski" varsayımıyla okunmuştu. Sonuç: ilk ve son tarih ters çıkıyordu. Kalıcı çözüm: sıraya güvenmek yerine tarihlerin `min` ve `max` değerini almak.

## 4. Metin tarihleri sıralanmıyordu

Kartları son commit'e göre sıralayan kod, `toordinal()` çağırıyordu; tarih `date` değil ISO **metni** olduğunda bu çağrı yoktu ve sıralama sessizce devre dışı kalıyordu. Test, gerçek veri türüyle (metin tarih) yazılana kadar yeşil görünüyordu.

## 5. Kesilen mesaj kaçışlanınca sınırı aşıyordu

Bir Telegram mesajını 4096 karakter sınırına göre kesen kod, kesmeyi **kaçışlamadan önce** yapıyordu; MarkdownV2 kaçışı karakter sayısını artırınca mesaj yine sınırı aşıyordu. Kesmeyi kaçışlanmış uzunluk üzerinden yapmak gerekti.

## Çıkardığım kural

- Ajan "bitti" derse bu, testin yeşil olduğunu kanıtlamaz. Testi kendin çalıştır.
- Ajanın yazdığı testler de ajanın yanlış varsayımlarını paylaşır: yanlış beklentileri kodla birlikte yazmış olabilir. Birkaç testi elle bozup gerçekten kırılıp kırılmadığına bak.
- Çekirdek mantığı, özellikle güvenlikle ilgili olanı, kendin yaz ya da satır satır oku. Mekanik iskelet işini ajana bırak.
