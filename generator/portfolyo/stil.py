"""Proje dosyası: yerel yazı tipleriyle, JavaScript gerektirmeyen portfolyo stili."""

CSS = """
@font-face { font-family: "Barlow"; font-weight: 400; font-style: normal; font-display: swap;
  src: url("/fonts/barlow-400-latin.woff2") format("woff2");
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }
@font-face { font-family: "Barlow"; font-weight: 400; font-style: normal; font-display: swap;
  src: url("/fonts/barlow-400-latin-ext.woff2") format("woff2");
  unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }
@font-face { font-family: "Barlow"; font-weight: 600; font-style: normal; font-display: swap;
  src: url("/fonts/barlow-600-latin.woff2") format("woff2");
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }
@font-face { font-family: "Barlow"; font-weight: 600; font-style: normal; font-display: swap;
  src: url("/fonts/barlow-600-latin-ext.woff2") format("woff2");
  unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }
@font-face { font-family: "Barlow"; font-weight: 700; font-style: normal; font-display: swap;
  src: url("/fonts/barlow-700-latin.woff2") format("woff2");
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD; }
@font-face { font-family: "Barlow"; font-weight: 700; font-style: normal; font-display: swap;
  src: url("/fonts/barlow-700-latin-ext.woff2") format("woff2");
  unicode-range: U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF; }

:root {
  color-scheme: light dark;
  --paper: #f8fafb;
  --surface: #ffffff;
  --ink: #173b56;
  --body: #273f50;
  --muted: #4b5e70;
  --accent: #2e6659;
  --accent-hover: #214c42;
  --rule: #d4dfe5;
  --selection: #d4e8e1;
  --font: "Barlow", system-ui, sans-serif;
  --max: 1120px;
  --gutter: clamp(22px, 5vw, 64px);
}
@media (prefers-color-scheme: dark) {
  :root {
    --paper: #111e29; --surface: #162633; --ink: #e3edf4;
    --body: #d0dde6; --muted: #acbfce; --accent: #a2d7c1;
    --accent-hover: #c6ecdc; --rule: #3a5060; --selection: #285449;
  }
}
* { box-sizing: border-box; }
html { scroll-padding-top: 24px; scrollbar-color: var(--muted) var(--paper); }
@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }
body { margin: 0; background: var(--paper); color: var(--body); font: 400 17px/1.65 var(--font); }
::selection { background: var(--selection); color: var(--ink); }
a { color: var(--accent); text-decoration-thickness: 1px; text-underline-offset: .22em; }
a:hover { color: var(--accent-hover); text-decoration-thickness: 2px; }
a:focus-visible, summary:focus-visible { outline: 2px solid var(--accent); outline-offset: 5px; border-radius: 2px; }
p { margin: 0 0 1rem; }
h1, h2, h3, h4 { color: var(--ink); line-height: 1.2; font-weight: 600; text-wrap: balance; }
h1 { margin: 0 0 10px; font-size: clamp(2rem, 3.2vw, 3rem); letter-spacing: -.025em; font-weight: 700; }
h2 { margin: 0 0 20px; font-size: 1.6rem; letter-spacing: -.015em; }
h3 { margin: 0 0 12px; font-size: 1.35rem; }
h4 { margin: 0 0 8px; font-size: 1rem; }
ul, ol { padding-left: 1.3em; }
svg { width: 18px; height: 18px; flex: 0 0 auto; vertical-align: middle; }
.raf { width: min(calc(100% - 2 * var(--gutter)), var(--max)); margin-inline: auto; }
main.raf { padding-bottom: 48px; }
.serit { border-bottom: 1px solid var(--rule); }
.serit .yuz { min-height: 82px; display: flex; align-items: center; gap: 26px; }
.serit .unit { margin: 0; border: 0; }
.marka { margin-right: auto; color: var(--ink); font-size: 20px; font-weight: 700; text-decoration: none; white-space: nowrap; }
.menu { display: flex; flex-wrap: wrap; gap: 4px 18px; list-style: none; margin: 0; padding: 0; font-size: 15px; }
.menu a { display: inline-flex; align-items: center; min-height: 44px; color: var(--muted); text-decoration: none; }
.menu a:hover { color: var(--accent); text-decoration: underline; }
.dil { display: flex; align-items: center; gap: 10px; font-size: 14px; white-space: nowrap; }
.dil a, .dil span { display: inline-flex; align-items: center; min-height: 44px; }
.dil [aria-current] { color: var(--ink); font-weight: 600; }
.unit { margin: 0 0 44px; }
.hero { padding-block: 48px 38px; margin-bottom: 0; }
.hero .yuz { display: grid; grid-template-columns: 1.05fr 1fr; gap: 56px; align-items: start; }
.hero .pitch { max-width: 66ch; margin: 0 0 15px; }
.hero .yuz > div:last-child { padding-top: 8px; }
.unvan { margin: 0 0 14px; font-size: 22px; color: var(--muted); line-height: 1.35; }
.konum { display: inline-block; color: var(--muted); margin: 0 0 12px 14px; font-size: 15px; }
.ledler { display: inline-flex; flex-wrap: wrap; gap: 12px; list-style: none; margin: 0 0 12px; padding: 0; color: var(--accent); font-size: 15px; }
.pr-durum { display: flex; margin-block: 12px; }
.tuslar, .baglar { display: flex; flex-wrap: wrap; align-items: center; gap: 8px 12px; }
.tus { display: inline-flex; gap: 8px; align-items: center; justify-content: center; min-height: 44px; padding: 8px 12px; border: 1px solid var(--rule); border-radius: 5px; color: var(--ink); font-size: 15px; line-height: 1.35; text-decoration: none; }
.tus:hover { color: var(--accent); border-color: var(--accent); text-decoration: none; }
.tus--eylem { background: var(--accent); color: var(--surface); border-color: var(--accent); font-weight: 600; }
.tus--eylem:hover { background: var(--accent-hover); color: var(--surface); }
.tus--kucuk { font-size: 14px; }
.cv-not { color: var(--muted); font-size: 13px; margin: 12px 0 0; }
.cv-not a { display: inline-block; padding-block: 6px; }
.ray { display: flex; align-items: baseline; justify-content: space-between; gap: 20px; margin-bottom: 14px; }
.ray h2 { margin: 0; }
.ray p { margin: 0; font-size: 14px; color: var(--muted); }
.ray--raf { padding-top: 10px; }
.one { margin: 0; border-top: 1px solid var(--rule); }
.one .yuz { display: grid; grid-template-columns: 1.45fr 1fr; gap: 64px; padding-block: 30px; }
.one + .iki { margin-top: 42px; }
.pr-ad { font-size: 1.75rem; letter-spacing: -.015em; margin: 0 0 12px; overflow-wrap: anywhere; }
.pr-ad a { color: var(--ink); text-decoration: none; }
.pr-ad a:hover { color: var(--accent); text-decoration: underline; }
.pr-aciklama { max-width: 68ch; margin: 0; }
.proje-detay h4 { color: var(--muted); }
.yigin { display: flex; flex-wrap: wrap; column-gap: 14px; row-gap: 3px; padding: 0; margin: 8px 0 16px; list-style: none; font-size: 14px; color: var(--muted); }
.baglar .tus { border: 0; padding: 8px 0; color: var(--accent); text-decoration: underline; text-underline-offset: .22em; }
.satir { display: grid; grid-template-columns: 1fr 1.8fr auto; gap: 24px; padding-block: 22px; border-top: 1px solid var(--rule); }
.satir h4 { font-size: 1.1rem; overflow-wrap: anywhere; }
.satir h4 a { color: var(--ink); text-decoration: none; }
.satir h4 a:hover { color: var(--accent); text-decoration: underline; }
.satir p { margin: 0; }
.satir .yigin { margin-bottom: 0; }
.alt { margin: 28px 0 12px; color: var(--muted); font-size: 16px; }
.iki { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; border-top: 1px solid var(--rule); padding-top: 32px; }
.iki .unit { margin-bottom: 40px; }
.kayit { margin-top: 18px; }
.kayit h3 { margin: 0 0 5px; font-size: 1.15rem; }
.kurum { margin: 0 0 4px; }
.tarih, .ek { display: block; color: var(--muted); font-size: 14px; font-variant-numeric: tabular-nums; }
.kayit > p:last-child { margin-top: 12px; }
.yetenek { margin: 24px 0 0; }
.yetenek > div { display: grid; grid-template-columns: 1fr 2.2fr; gap: 16px 40px; margin-bottom: 16px; }
.yetenek dt { font-weight: 600; color: var(--ink); }
.yetenek dd { margin: 0; color: var(--muted); }
.yetenek ul { display: flex; flex-wrap: wrap; gap: 4px 18px; list-style: none; padding: 0; margin: 0; }
.yazi-listesi { padding: 0; margin: 24px 0; list-style: none; }
.yazi-listesi li { padding-block: 18px; border-top: 1px solid var(--rule); }
.yazi-baslik { font-weight: 600; font-size: 1.2rem; }
.yazi-listesi time { display: block; font-size: 14px; color: var(--muted); }
.yazi-listesi p { margin: 8px 0 0; }
.yazi { padding-top: 40px; }
.yazi article { max-width: 70ch; margin-inline: auto; overflow-wrap: anywhere; }
.yazi h1 { margin-top: 22px; }
.yazi h2 { margin: 38px 0 15px; }
.yazi h3 { margin: 28px 0 12px; }
.yazi pre { overflow-x: auto; max-width: 100%; background: var(--surface); padding: 18px; border-radius: 5px; font-size: 14px; }
.yazi code { font-family: Consolas, monospace; }
.yazi table { display: block; max-width: 100%; overflow-x: auto; border-collapse: collapse; }
.yazi th, .yazi td { padding: 8px 12px; border-bottom: 1px solid var(--rule); text-align: left; }
.yazi blockquote { margin-inline: 0; padding-inline: 20px; border-left: 1px solid var(--rule); color: var(--muted); }
.yazi-meta, .geri { color: var(--muted); font-size: 14px; }
.yazi-gezinme { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 20px; padding-top: 24px; margin-top: 40px; border-top: 1px solid var(--rule); }
.yazi-gezinme a { padding-block: 12px; }
.iletisim { padding-top: 32px; border-top: 1px solid var(--rule); margin-bottom: 0; }
.iletisim .yuz { display: grid; grid-template-columns: 1fr auto; gap: 40px; align-items: center; }
.iletisim p { max-width: 65ch; margin-bottom: 0; }
.tus--posta { overflow-wrap: anywhere; max-width: 100%; }
.alt-not { width: min(calc(100% - 2 * var(--gutter)), var(--max)); margin: 0 auto; padding-block: 22px 32px; border-top: 1px solid var(--rule); color: var(--muted); font-size: 13px; }
.skip { position: absolute; left: 16px; top: -100px; padding: 12px; background: var(--surface); color: var(--accent); z-index: 10; }
.skip:focus { top: 12px; }
.proje-gorseller { grid-column: 1 / -1; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr)); gap: 24px; }
.proje-gorseller figure { margin: 0; min-width: 0; }
.proje-gorseller a { display: flex; justify-content: center; background: var(--surface); border: 1px solid var(--rule); border-radius: 5px; overflow: hidden; }
.proje-gorseller img { display: block; max-width: 100%; width: auto; height: auto; max-height: 500px; object-fit: contain; object-position: top center; }
.proje-gorseller .goruntu--ust img { width: 100%; height: clamp(220px, 36vw, 480px); max-height: none; object-fit: cover; }
.proje-gorseller figcaption { margin-top: 10px; font-size: 14px; color: var(--muted); }
.satir .proje-gorseller { max-width: 800px; }
@media (max-width: 950px) {
  .serit .yuz { flex-wrap: wrap; gap: 4px 20px; padding-block: 12px; }
  .menu { order: 4; flex-basis: 100%; gap: 2px 20px; }
  .hero .yuz, .one .yuz, .iki { gap: 32px; }
  .iletisim .yuz { grid-template-columns: 1fr; gap: 20px; }
}
@media (max-width: 640px) {
  body { font-size: 16px; }
  .hero { padding-block: 30px; }
  .hero .yuz, .one .yuz, .iki, .satir, .yetenek > div { grid-template-columns: 1fr; }
  .hero .yuz { gap: 24px; }
  .hero .yuz > div:last-child { padding-top: 0; }
  .hero .tuslar { gap: 8px; }
  .one .yuz { gap: 20px; padding-block: 26px; }
  .proje-detay h4 { font-size: 14px; }
  .iki { gap: 0; padding-top: 28px; }
  .satir { gap: 10px; padding-block: 22px; }
  .satir .baglar { margin-top: 0; }
  .yetenek > div { gap: 8px; }
  .yetenek dd { margin-bottom: 16px; }
  .ray { align-items: start; }
  .iletisim .tuslar { align-items: start; }
  .tus--posta { font-size: 14px; }
}
@media print {
  :root { color-scheme: light; --paper: #fff; --surface: #fff; --ink: #173b56; --body: #273f50; --muted: #4b5e70; --accent: #2e6659; --rule: #d4dfe5; }
  .serit, .skip, .hero .tuslar, .alt-not { display: none; }
  .raf { width: 100%; }
  .unit, .one, .iki { break-inside: avoid; }
  body { font-size: 11pt; }
}
"""
