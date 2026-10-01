---
baslik: uvicorn SIGTERM'de atexit çalıştırmaz
tarih: 2026-10-01
ozet: Bir başlatıcı betik alt süreçleri atexit ile temizliyordu. kill ile durdurunca süreçler öksüz kaldı; çözüm tek satırlık bir sinyal işleyicisi.
etiketler: [python, uvicorn, süreç]
herkese_acik: false
---
Bir başlatıcı betik, alt süreç olarak birkaç küçük web sunucusu açıyordu ve çıkışta hepsini `atexit` ile kapatıyordu. Betik `uvicorn` ile ayağa kalkıyordu. `Ctrl+C` ile her şey temiz kapanıyordu. Ama `kill <pid>` (yani SIGTERM) ile durdurunca alt süreçler **öksüz** kalıyordu: hâlâ port tutuyorlardı.

## Ne oluyor

SIGTERM için Python'da varsayılan davranış, süreci yorumlayıcı kapanışını çalıştırmadan sonlandırmaktır. `atexit` işleyicileri yalnızca *normal* çıkışta (ya da `sys.exit`) çalışır. uvicorn sinyali yakalayıp sunucuyu düzgün kapatıyor, sonra sinyali yeniden yükseltiyor. Betiğin kendisinde bir işleyici yoksa süreç varsayılan davranışla ölüyor ve `atexit` hiç devreye girmiyor.

Bunu gerçek bir süreçle doğruladım: sunucuyu başlat, `kill` gönder, alt süreçlerin PID'lerine bak. Birim testle yakalanmaz, çünkü sorun işletim sistemi sinyalinin yolunda.

## Çözüm

SIGTERM'i normal bir çıkışa çevir:

```python
import signal
import sys

signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))
```

`sys.exit(0)` bir `SystemExit` fırlatır, yorumlayıcı normal kapanışa geçer ve `atexit` işleyicileri çalışır.

## Notlar

- Windows'ta SIGTERM semantiği farklıdır; orada `signal.SIGBREAK` ve süreç grupları devreye girer. Bu not Linux davranışı içindir.
- İşleyici ana iş parçacığında kurulmalıdır (`signal.signal` başka bir iş parçacığında hata verir).
- Daha sağlam bir seçenek, alt süreçleri bir süreç grubuna koyup grubu öldürmektir. Ama mevcut yapıyı bozmadan en küçük düzeltme yukarıdaki satırdır.
