# Modulio Website - Odoo 17 Landing Page Module

> **Streamlining Business. Simplifying Success.**

Modul Odoo 17 yang menyediakan landing page lengkap untuk Modulio - Odoo Solution Expert.

---

## 📋 Informasi Modul

| Atribut | Detail |
|---------|--------|
| **Nama** | Modulio Website - Landing Page |
| **Versi** | 17.0.1.0.0 |
| **Kategori** | Website |
| **Dependencies** | website, website_crm, crm |
| **License** | LGPL-3 |

---

## ✨ Fitur

### 12 Sections Lengkap

1. **Hero Section** - Headline fokus pada outcome bisnis
2. **Partners Section** - Logo partner teknologi global (Odoo, PostgreSQL, Python, Cloud)
3. **Pain Points** - 3 masalah utama yang dipecahkan
4. **Services** - Accounting, HR, Custom Development
5. **Portfolio** - 3 case studies dengan angka keberhasilan
6. **Testimonials** - Kutipan dari klien nyata
7. **Team Profile** - Shaffan, Ilan, Erlan, Chaca
8. **Process** - 4 langkah: Discovery → Design → Implementation → Scaling
9. **FAQ** - 6 pertanyaan umum (harga, waktu, keamanan, integrasi)
10. **CTA Form** - Lead capture terintegrasi Odoo CRM
11. **Footer** - Informasi kontak dan links
12. **Navbar** - Navigasi dengan smooth scroll

### Integrasi CRM
- Form lead capture otomatis membuat lead di Odoo CRM
- Field mapping: Nama, Perusahaan, Email, Telepon, Jumlah Karyawan, Modul yang Diminati
- Notifikasi email untuk tim sales

### Responsive Design
- Mobile-first approach
- Optimized untuk tablet dan desktop
- Touch-friendly navigation

---

## 🎨 Brand Identity

| Warna | HEX | Penggunaan |
|-------|-----|------------|
| **Navy** | `#1b3d5a` | Primary, Headers, Text |
| **Coral** | `#f26c5f` | CTA, Buttons, Accents |
| **Off White** | `#f2f2f3` | Backgrounds |
| **Text Dark** | `#2c3e50` | Body text |

---

## 🚀 Instalasi

### 1. Copy Modul
```bash
cp -r modulio_website /path/to/odoo/addons/
```

### 2. Update Apps List
- Buka Odoo → Apps → Update Apps List
- Atau via command line:
```bash
./odoo-bin -u all -d your_database
```

### 3. Install Modul
- Cari "Modulio Website" di Apps
- Klik Install

### 4. Akses Landing Page
Buka: `http://your-odoo-instance/modulio-landing`

---

## ⚙️ Konfigurasi

### Theme Colors
Setelah instalasi, ubah warna theme di:
```
Website → Edit → Theme → Colors
- Primary: #1b3d5a
- Secondary: #f26c5f
```

### CRM Integration
Form otomatis terhubung ke CRM. Konfigurasi tambahan:
```
CRM → Configuration → Settings → Lead Assignment
```

### Menu Management
Menu otomatis dibuat. Untuk mengubah:
```
Website → Configuration → Menus
```

---

## 📝 Customisasi

### Edit Konten
1. Aktifkan Edit Mode di website
2. Klik elemen yang ingin diubah
3. Edit teks, gambar, atau styling
4. Save

### Ganti Gambar
Upload gambar ke:
```
/static/images/
```

Gambar yang diperlukan:
- `hero-dashboard.png` - Hero section image
- `partner-*.png` - Partner logos (6 gambar)
- `case-study-*.jpg` - Portfolio images (3 gambar)
- `team-*.jpg` - Team photos (4 gambar)
- `avatar-*.jpg` - Testimonial avatars (2 gambar)

### Custom CSS
Tambahkan CSS di:
```
Website → Edit → Customize → Custom CSS
```

---

## 🗂️ Struktur Modul

```
modulio_website/
├── __init__.py
├── __manifest__.py
├── README.md
├── models/
│   └── __init__.py
├── controllers/
│   └── __init__.py
├── data/
│   └── website_menu.xml
├── security/
│   └── ir.model.access.csv
├── static/
│   ├── description/
│   │   └── index.html
│   ├── images/          # Upload gambar di sini
│   └── src/
│       ├── scss/
│       │   ├── modulio_theme.scss
│       │   └── snippets.scss
│       └── js/
│           └── modulio.js
└── views/
    ├── assets.xml
    ├── landing_page_template.xml
    ├── snippets_options.xml
    └── snippets/
        ├── s_hero.xml
        ├── s_partners.xml
        ├── s_pain_points.xml
        ├── s_services.xml
        ├── s_portfolio.xml
        ├── s_testimonials.xml
        ├── s_team.xml
        ├── s_process.xml
        ├── s_faq.xml
        └── s_cta_form.xml
```

---

## 🔧 Troubleshooting

### Form tidak terkirim
- Pastikan modul `website_crm` terinstall
- Check CRM → Settings → Lead Assignment
- Verify email server configuration

### Gambar tidak muncul
- Upload gambar ke `/static/images/`
- Check file permissions
- Clear browser cache

### Styling tidak berubah
- Restart Odoo server
- Clear browser cache
- Check browser console untuk errors

---

## 📞 Support

Untuk pertanyaan atau bantuan:
- Email: hello@modulio.com
- Website: https://modulio.com

---

## 📄 License

LGPL-3

---

**Modulio © 2024** | Transformasi Digital untuk Bisnis Indonesia
