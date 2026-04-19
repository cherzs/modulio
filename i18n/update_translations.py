#!/usr/bin/env python3
"""Script to update Indonesian translations in id.po file."""

import re

# Translation dictionary - English to Indonesian
translations = {
    # Navigation
    "Services": "Layanan",
    "Approach": "Pendekatan",
    "Work": "Portofolio",
    "Contact": "Kontak",
    "Book consultation": "Jadwalkan Konsultasi",
    
    # Hero Section
    "Accounting systems": "Sistem Akuntansi",
    "Odoo": "Odoo",
    "Integrations": "Integrasi",
    "Accounting systems,": "Sistem akuntansi,",
    "engineered for clarity.": "dirancang untuk kejelasan.",
    "Implementations delivered": "Implementasi selesai",
    "Avg. reduction in close time": "Rata-rata pengurangan waktu closing",
    "Industries served": "Industri dilayani",
    "Client retention": "Retensi klien",
    "Explore our services": "Jelajahi layanan kami",
    "Book a consultation": "Jadwalkan konsultasi",
    
    # Services Section
    "A focused practice across four disciplines.": "Praktik terfokus di empat disiplin.",
    "A focused practice across four": "Praktik terfokus di empat",
    "disciplines.": "disiplin.",
    " disciplines.": " disiplin.",
    "Accounting setup with Odoo": "Setup Akuntansi dengan Odoo",
    "ERP customization": "Kustomisasi ERP",
    "Web application development": "Pengembangan aplikasi web",
    "System integration": "Integrasi sistem",
    "Localized compliance": "Kepatuhan lokal",
    "Multi-currency": "Multi-mata uang",
    "Audit-ready reporting": "Laporan siap audit",
    "Workflow design": "Desain alur kerja",
    "Custom modules": "Modul kustom",
    "Internal tools": "Alat internal",
    "Client portals": "Portal klien",
    "API-first architecture": "Arsitektur API-first",
    "Bank & payment APIs": "API Bank & pembayaran",
    "Bank &amp; payment APIs": "API Bank & pembayaran",
    "CRM & e-commerce sync": "Sinkronisasi CRM & e-commerce",
    "CRM &amp; e-commerce sync": "Sinkronisasi CRM & e-commerce",
    "Data pipelines": "Pipeline data",
    "Role &amp; access architecture": "Arsitektur role & akses",
    "Role & access architecture": "Arsitektur role & akses",
    
    # Testimonials
    "Client Reviews": "Ulasan Klien",
    "What our clients say about working with us.": "Apa kata klien tentang bekerja dengan kami.",
    "Real feedback from finance leaders and operations teams who transformed their systems with Modulio.": "Umpan balik nyata dari pemimpin keuangan dan tim operasi yang mentransformasi sistem mereka dengan Modulio.",
    
    # Why Choose Us
    "Why Modulio": "Mengapa Modulio",
    "A consulting partner —": "Mitra konsultan —",
    "A consulting partner &#x2014;": "Mitra konsultan —",
    "not a vendor.": "bukan vendor.",
    "System thinking": "Berpikir sistematis",
    "Reliability first": "Keandalan utama",
    "Efficiency by design": "Efisiensi by design",
    "Senior consultants": "Konsultan senior",
    
    # Process/How We Work
    "How We Work": "Cara Kami Bekerja",
    "A structured approach to every engagement.": "Pendekatan terstruktur untuk setiap proyek.",
    "Discovery": "Penemuan",
    "Design": "Desain",
    "Build": "Bangun",
    "Launch": "Peluncuran",
    "Stakeholder interviews": "Wawancara stakeholder",
    "Process documentation": "Dokumentasi proses",
    "Gap analysis": "Analisis gap",
    "Solution architecture": "Arsitektur solusi",
    "Technical specification": "Spesifikasi teknis",
    "Agile development": "Pengembangan Agile",
    "Weekly demos": "Demo mingguan",
    "Iterative refinement": "Penyempurnaan iteratif",
    "Team training": "Pelatihan tim",
    "Data migration": "Migrasi data",
    "Go-live support": "Dukungan go-live",
    
    # Portfolio
    "Selected Work": "Karya Terpilih",
    "Outcomes our clients can measure.": "Hasil yang dapat diukur klien kami.",
    "Manufacturing": "Manufaktur",
    "Professional Services": "Layanan Profesional",
    "E-Commerce": "E-Commerce",
    "Retail": "Ritel",
    "Logistics": "Logistik",
    "faster month-end close": "closing bulanan lebih cepat",
    "manual entries automated": "entri manual terotomasi",
    "systems unified": "sistem terintegrasi",
    "View all case studies": "Lihat semua studi kasus",
    "View all projects": "Lihat semua proyek",
    
    # CTA
    "Begin a Conversation": "Mulai Percakapan",
    "Let's design the system your finance team deserves.": "Mari rancang sistem yang layak untuk tim keuangan Anda.",
    "Email": "Email",
    "Phone": "Telepon",
    "Office": "Kantor",
    
    # Footer
    "Accounting systems · Odoo · Integrations": "Sistem Akuntansi · Odoo · Integrasi",
    "Accounting systems &#xB7; Odoo &#xB7; Integrations": "Sistem Akuntansi · Odoo · Integrasi",
    "All rights reserved.": "Hak cipta dilindungi.",
    
    # Service Pages
    "Features": "Fitur",
    "What's Included": "Yang Termasuk",
    "What&#x2019;s Included": "Yang Termasuk",
    "Learn more": "Pelajari lebih lanjut",
    "Accounting setup": "Setup Akuntansi",
    "with Odoo.": "dengan Odoo.",
    "HR systems,": "Sistem HR,",
    "built for scale.": "dibangun untuk skala.",
    "ERP customization,": "Kustomisasi ERP,",
    "without the fork.": "tanpa fork.",
    "faster close": "closing lebih cepat",
    "tax compliance": "kepatuhan pajak",
    "entries automated": "entri terotomasi",
    "financial visibility": "visibilitas keuangan",
    "payroll processing": "proses payroll",
    "labor compliance": "kepatuhan ketenagakerjaan",
    "employees managed": "karyawan dikelola",
    "payroll errors": "kesalahan payroll",
    "implementations": "implementasi",
    "industries served": "industri dilayani",
    "custom modules": "modul kustom",
    "client satisfaction": "kepuasan klien",
    
    # Common
    "Start similar project": "Mulai proyek serupa",
    "View all cases": "Lihat semua kasus",
    "No projects found": "Tidak ada proyek ditemukan",
    "Check back soon for new case studies.": "Periksa kembali segera untuk studi kasus baru.",
    "View All Projects": "Lihat Semua Proyek",
    "Related Work": "Karya Terkait",
    "Similar engagements": "Proyek serupa",
    "Our Portfolio": "Portofolio Kami",
    "Our Services": "Layanan Kami",
    
    # Additional phrases
    "The Results": "Hasil",
    "The Challenge": "Tantangan",
    "Our Approach": "Pendekatan Kami",
    "Project Overview": "Gambaran Proyek",
    "Industry": "Industri",
    "Duration": "Durasi",
    "months": "bulan",
    "Client": "Klien",
    "Read case study": "Baca studi kasus",
    "CASE": "KASUS",
}

def update_po_file(input_file, output_file):
    """Update PO file with translations."""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Process each translation
    for eng, ind in translations.items():
        # Pattern to match msgid "text" followed by msgstr ""
        pattern = f'msgid "{eng}"\nmsgstr ""'
        replacement = f'msgid "{eng}"\nmsgstr "{ind}"'
        content = content.replace(pattern, replacement)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {output_file}")

if __name__ == "__main__":
    update_po_file('id.po', 'id.po')
    print("Translation update complete!")
