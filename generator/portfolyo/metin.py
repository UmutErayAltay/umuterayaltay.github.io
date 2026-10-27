"""Arayüz metinleri (TR/EN). İçerik (ad, açıklama, deneyim) yapılandırmadan gelir; burada yalnız sabit etiketler var."""

from __future__ import annotations

DILLER = ("tr", "en")

_TR = {
    "atla": "İçeriğe geç",
    "sayfa_bolumleri": "Sayfa bölümleri",
    "dil_etiket": "Dil",
    "menu_projeler": "Projeler",
    "menu_deneyim": "Deneyim",
    "menu_yetenekler": "Yetenekler",
    "menu_egitim": "Eğitim",
    "menu_yazilar": "Yazılar",
    "menu_iletisim": "İletişim",
    "cv_kisa": "CV",
    "cv_indir": "CV indir",
    "cv_etiket": "CV:",
    "cv_tr": "Türkçe (PDF)",
    "cv_en": "English (PDF)",
    "teknoloji": "Teknolojiler",
    "eposta": "E-posta",
    "oneci_baslik": "Seçili projeler",
    "oneci_alt": "",
    "diger_baslik": "Diğer projeler",
    "deneyim_baslik": "Deneyim",
    "egitim_baslik": "Eğitim",
    "yetenek_baslik": "Araçlar ve çalışma biçimi",
    "yazi_baslik": "Yazılar",
    "commit": "commit",
    "son_commit": "Son commit:",
    "hafta_once": "12 hafta önce",
    "bu_hafta": "bu hafta",
    "olcer_aria": "Son 12 haftada commit sayısı:",
    "hic_commit": "hiç commit yok",
    "olcer_toplam": "Commit etkinliği · son 12 hafta",
    "iletisim_baslik": "İletişim",
    "iletisim_metin": "Junior pozisyonlar ve projeler için e-posta ya da LinkedIn üzerinden ulaşabilirsin.",
    "uretildi": "Otomatik üretildi:",
    "ana_sayfa": "← Ana sayfa",
    "dk_okuma": "dk okuma",
    "diger_yazilar": "Diğer yazılar",
    "locale": "tr_TR",
}

_EN = {
    "atla": "Skip to content",
    "sayfa_bolumleri": "Page sections",
    "dil_etiket": "Language",
    "menu_projeler": "Projects",
    "menu_deneyim": "Experience",
    "menu_yetenekler": "Skills",
    "menu_egitim": "Education",
    "menu_yazilar": "Writing",
    "menu_iletisim": "Contact",
    "cv_kisa": "CV",
    "cv_indir": "Download CV",
    "cv_etiket": "CV:",
    "cv_tr": "Türkçe (PDF)",
    "cv_en": "English (PDF)",
    "teknoloji": "Technologies",
    "eposta": "Email",
    "oneci_baslik": "Selected projects",
    "oneci_alt": "",
    "diger_baslik": "Other projects",
    "deneyim_baslik": "Experience",
    "egitim_baslik": "Education",
    "yetenek_baslik": "Tools and working methods",
    "yazi_baslik": "Writing",
    "commit": "commits",
    "son_commit": "Last commit:",
    "hafta_once": "12 weeks ago",
    "bu_hafta": "this week",
    "olcer_aria": "Commits per week over the last 12 weeks:",
    "hic_commit": "no commits",
    "olcer_toplam": "Commit activity · last 12 weeks",
    "iletisim_baslik": "Contact",
    "iletisim_metin": "You can reach me by email or LinkedIn about junior roles and projects.",
    "uretildi": "Generated automatically:",
    "ana_sayfa": "← Home",
    "dk_okuma": "min read",
    "diger_yazilar": "More posts",
    "locale": "en_US",
}

METIN = {"tr": _TR, "en": _EN}


def m(dil: str, anahtar: str) -> str:
    """Etiket döndürür; bilinmeyen dil Türkçeye düşer, bilinmeyen anahtar KeyError (testle yakalanır)."""
    return METIN.get(dil, _TR)[anahtar]
