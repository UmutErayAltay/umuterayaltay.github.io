# umuterayaltay.github.io

Kişisel portfolyo sitesi: https://umuterayaltay.github.io (Türkçe) · https://umuterayaltay.github.io/en/ (English)

Site elle yazılmaz; `portfolyo.json` (Türkçe), `portfolyo.en.json` (İngilizce), `yazilar/*.md` (yazılar, yalnız Türkçe)
ve `generator/` (üretici) kaynaklarından **GitHub Actions** ile üretilip yayınlanır (`.github/workflows/yayinla.yml`).
Üretilmiş HTML bu repoya commit'lenmez.

- Yayın öncesinde projelerin herkese açık olduğu GitHub API üzerinden kontrol edilir; özel repo yayınlanmaz. Commit sayaçları ve etkinlik grafikleri arayüzde gösterilmez.
- Yayın her push'ta ve her Pazartesi otomatik çalışır; Actions sekmesinden elle de tetiklenebilir.
- İçerik: deneyim, eğitim, yetenekler, iletişim ve CV bağlantıları `portfolyo*.json` içindedir. `one_cikan: true` olan projeler üstte görünür; deneyim ve eğitim bunları izler. Diğer projeler daha aşağıda listelenir.
- `statik/` olduğu gibi siteye kopyalanır: `statik/cv/` (CV PDF'leri), `statik/fonts/` (Barlow, SIL OFL 1.1, lisans: `OFL.txt`). CV'yi güncellemek için aynı adlı PDF'in üzerine yaz.
- Yazı eklemek için `yazilar/` altına `ad-soyad.md` koy; frontmatter'da `herkese_acik: true` yoksa taslak sayılır ve yayınlanmaz.
- Yayın öncesi üretici testleri koşar; bir repo için veri alınamazsa (`--siki`) yayın yapılmaz, eski site kalır.
- Her sayfa yayından önce sızıntı denetiminden geçer (özel anahtar, yerel yol, dış kaynak, yapılandırmadaki dışında e-posta); site JavaScript'siz ve dış kaynaksızdır.
- Paylaşım görselleri (`og/*.png`) ve `feed.xml` yayın sırasında üretilir.
- `generator/` özel bir depodan kopyalanmıştır; bkz. `generator/KAYNAK.txt` (güncelleme: araclar'daki `tools/portfolyo_yayinla.py`).

Yerel önizleme (Windows/PowerShell örneği, bu reponun kökünden):

```
$env:PYTHONPATH = "generator"
python -m portfolyo uret portfolyo.json --api --yazilar yazilar --cikti _site
python -m portfolyo uret portfolyo.en.json --api --cikti _site/en
Copy-Item statik\* _site -Recurse -Force
python -m http.server 8000 -d _site
```

Proje görüntüleri `statik/projeler/` altında aynı kökenden sunulur; kaynaklar ve demo/tarihsel görüntü ayrımları [KAYNAKLAR.md](statik/projeler/KAYNAKLAR.md) dosyasındadır. Üretilmiş taslak arayüzler gerçek uygulama görüntüsü olarak kullanılmaz.
