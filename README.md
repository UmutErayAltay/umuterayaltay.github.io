# umuterayaltay.github.io

Kişisel portfolyo sitesi: https://umuterayaltay.github.io

Site elle yazılmaz; `portfolyo.json` (proje listesi), `yazilar/*.md` (yazılar) ve `generator/`
(üretici) kaynaklarından **GitHub Actions** ile üretilip yayınlanır (`.github/workflows/yayinla.yml`).
Üretilmiş HTML bu repoya commit'lenmez.

- Proje kartlarındaki istatistikler GitHub API'sinden alınır (yalnız herkese açık repolar; özel repo asla yayınlanmaz).
- Yayın her push'ta ve her Pazartesi otomatik çalışır; Actions sekmesinden elle de tetiklenebilir.
- Yazı eklemek için `yazilar/` altına `ad-soyad.md` koy; frontmatter'da `herkese_acik: true` yoksa taslak sayılır ve yayınlanmaz.
- `generator/` özel bir depodan kopyalanmıştır; bkz. `generator/KAYNAK.txt`.
