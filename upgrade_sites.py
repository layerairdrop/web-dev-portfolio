#!/usr/bin/env python3
"""Upgrade LYID demo sites with MotionSites premium cinematic design."""
import os, json, re

SITES_DIR = os.path.expanduser("~/LYID-BOTS/web-dev-portfolio/sites")
GA4 = "G-C6BH106VBQ"
WHATSAPP = "6287897299985"
PORTFOLIO_URL = "https://ralies.biz.id"

# Industry configs
CONFIGS = {
    "04-toko-online": {
        "name": "Batik Nusantara",
        "tagline": "Kain Batik Premium Indonesia",
        "desc": "Batik tulis dan cap premium dari pengrajin terbaik Indonesia. Setiap helai kain adalah karya seni.",
        "bg": "#faf8f4", "surface": "#fff", "text": "#2c1810", "muted": "#8b7355",
        "accent": "#8b4513", "accent2": "#a0522d", "gold": "#d4a574", "green": "#556b2f",
        "hero_bg": "linear-gradient(135deg, #1a0f0a 0%, #2c1810 50%, #3d2314 100%)",
        "hero_gradient": "radial-gradient(circle at 20% 50%, rgba(212,165,116,.12), transparent 50%), radial-gradient(circle at 80% 20%, rgba(139,69,19,.1), transparent 50%)",
        "hero_accent_grad": "linear-gradient(90deg, #d4a574, #8b4513)",
        "font_heading": "'Playfair Display', serif",
        "font_body": "'Poppins', system-ui, sans-serif",
        "features": [
            ("✅", "100% Batik Asli", "Tulis & cap original"),
            ("🚚", "Gratis Ongkir", "Min. pembelian Rp 500rb"),
            ("🔄", "Garansi 30 Hari", "Retur mudah & cepat"),
            ("💬", "Konsultasi Gratis", "Chat langsung ahli batik"),
        ],
        "products": [
            ("Batik Tulis Solo Motif Parang", "Solo, Jawa Tengah", "Rp 850.000", "Rp 1.200.000", "Baru", "https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17?w=400&q=80"),
            ("Kemeja Batik Pria Modern", "Pekalongan, Jawa Tengah", "Rp 350.000", "", "", "https://images.unsplash.com/photo-1534126416832-a88fdf2911c2?w=400&q=80"),
            ("Gamis Batik Elegan", "Yogyakarta", "Rp 475.000", "", "Best Seller", "https://images.unsplash.com/photo-1528459801416-a9e53bbf4e17?w=400&q=80&fit=crop&crop=center"),
            ("Tas Batik Kulit", "Cirebon, Jawa Barat", "Rp 285.000", "Rp 350.000", "", "https://images.unsplash.com/photo-1534126416832-a88fdf2911c2?w=400&q=80&fit=crop&crop=top"),
        ],
        "testimonials": [
            ("\"Kainnya sangat halus dan motifnya detail banget. Beda jauh sama batik factory. Worth it!\"", "— Ibu Dewi, Jakarta"),
            ("\"Pengiriman cepat, packaging rapi. Kemeja batiknya pas dipakai ke kantor. Banyak yang nanya beli dimana.\"", "— Pak Hendra, Surabaya"),
            ("\"Gamisnya cantik banget! Bahan adem, jahitan rapi. Sudah repeat order 3 kali.\"", "— Siti Nurhaliza, Bandung"),
        ],
        "footer_links": ["Batik Tulis", "Batik Cap", "Koleksi Pria", "Koleksi Wanita"],
        "help_links": ["Cara Order", "Pengiriman", "Retur & Refund", "FAQ"],
    },
    "properti-premium": {
        "name": "Nusantara Premium",
        "tagline": "Properti Eksklusif Indonesia",
        "desc": "Temukan hunian eksklusif di lokasi premium Indonesia. Investasi properti yang menguntungkan.",
        "bg": "#0f172a", "surface": "#1e293b", "text": "#f1f5f9", "muted": "#94a3b8",
        "accent": "#3b82f6", "accent2": "#8b5cf6", "gold": "#fbbf24", "green": "#10b981",
        "hero_bg": "linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #172554 100%)",
        "hero_gradient": "radial-gradient(circle at 30% 40%, rgba(59,130,246,.1), transparent 50%), radial-gradient(circle at 70% 60%, rgba(139,92,246,.08), transparent 50%)",
        "hero_accent_grad": "linear-gradient(90deg, #3b82f6, #8b5cf6)",
        "font_heading": "'Inter', sans-serif",
        "font_body": "'Inter', system-ui, sans-serif",
        "features": [
            ("🏠", "Premium Location", "Lokasi strategis dan elite"),
            ("💰", "High ROI", "Return on investment optimal"),
            ("🔒", "Legal Clear", "Sertifikat hak milik"),
            ("🤝", "Free Consult", "Konsultasi properti gratis"),
        ],
        "properties": [
            ("Villa Modern Nusantara", "Bali, Indonesia", "Rp 2.500.000.000", "Rp 3.200.000.000", "Featured"),
            ("Penthouse Skyline", "Jakarta Selatan", "Rp 5.800.000.000", "", "Premium"),
            ("Rumah Minimalis Tropis", "Bandung, Jawa Barat", "Rp 1.200.000.000", "", ""),
            ("Townhouse Elite", "Surabaya, Jawa Timur", "Rp 850.000.000", "Rp 1.100.000.000", "Hot"),
        ],
        "testimonials": [
            ("\"Investasi properti terbaik yang saya lakukan. Appreciation rate stabil dan lokasi strategis.\"", "— Bapak Rahmat, Investor"),
            ("\"Tim profesional, proses mulus dari survey hingga akad. Highly recommended!\"", "— Ibu Sari, Jakarta"),
            ("\"Property nya bagus banget, harga worth it. Pelayanan konsultatif luar biasa.\"", "— Pak Budi, Bandung"),
        ],
        "footer_links": ["Rumah", "Apartemen", "Villa", "Tanah"],
        "help_links": ["Proses Pembelian", "Pembiayaan", "Legalitas", "FAQ"],
    },
    "edu-academy": {
        "name": "EduAcademy",
        "tagline": "Platform Pembelajaran Online Terbaik",
        "desc": "Platform e-learning terbaik dengan 200+ kursus, mentor berpengalaman, dan sertifikat resmi.",
        "bg": "#ffffff", "surface": "#fff", "text": "#1e293b", "muted": "#64748B",
        "accent": "#4F46E5", "accent2": "#4338CA", "gold": "#F59E0B", "green": "#10b981",
        "hero_bg": "linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #1e40af 100%)",
        "hero_gradient": "radial-gradient(circle at 25% 50%, rgba(79,70,229,.15), transparent 50%), radial-gradient(circle at 75% 30%, rgba(245,158,11,.1), transparent 50%)",
        "hero_accent_grad": "linear-gradient(90deg, #4F46E5, #7C3AED)",
        "font_heading": "'Inter', sans-serif",
        "font_body": "'Inter', system-ui, sans-serif",
        "features": [
            ("📚", "200+ Kursus", "Berbagai bidang expertise"),
            ("🎓", "Mentor Ahli", "Pengajar berpengalaman"),
            ("📜", "Sertifikat Resmi", "Dikenal industri"),
            ("💻", "Flexible Learning", "Belajar kapan saja"),
        ],
        "courses": [
            ("Full Stack Web Development", "Programming", "Rp 499.000", "Rp 750.000", "Premium"),
            ("Data Science & Machine Learning", "Data Science", "Rp 599.000", "", "Best Seller"),
            ("Digital Marketing Masterclass", "Marketing", "Rp 299.000", "", ""),
            ("UI/UX Design Professional", "Design", "Rp 450.000", "Rp 650.000", "New"),
        ],
        "testimonials": [
            ("\"Kurikulumnya sangat update dan mentor nya supportive. Sekarang saya sudah kerja di startup ternama!\"", "— Rizky, Full Stack Developer"),
            ("\"EduAcademy membantu saya switch career dari accounting ke data science. Best investment ever!\"", "— Putri, Data Scientist"),
            ("\"Sertifikatnya diakui perusahaan besar. Fresh graduate dengan certified skills!\"", "— Ahmad, UI/UX Designer"),
        ],
        "footer_links": ["Kursus", "Mentor", "Sertifikat", "Karier"],
        "help_links": ["Cara Daftar", "Metode Bayar", "FAQ", "Bantuan"],
    },
    "grand-hotel": {
        "name": "Grand Hotel Bali",
        "tagline": "Pengalaman Kemewahan Tropis",
        "desc": "Nikmati liburan impian Anda di Grand Hotel Bali. Kemewahan tropis dengan pelayanan 5 bintang.",
        "bg": "#FFFBF5", "surface": "#fff", "text": "#1a1a1a", "muted": "#666",
        "accent": "#B8860B", "accent2": "#D4A843", "gold": "#B8860B", "green": "#10b981",
        "hero_bg": "linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 50%, #2d2416 100%)",
        "hero_gradient": "radial-gradient(circle at 30% 40%, rgba(184,134,11,.15), transparent 50%), radial-gradient(circle at 70% 60%, rgba(212,168,67,.1), transparent 50%)",
        "hero_accent_grad": "linear-gradient(90deg, #B8860B, #D4A843)",
        "font_heading": "'Inter', sans-serif",
        "font_body": "'Inter', sans-serif",
        "features": [
            ("🏖️", "Private Beach", "Akses pantai pribadi"),
            ("🍽️", "Fine Dining", "Restoran bintang 5"),
            ("💆", "Spa & Wellness", "Perawatan premium"),
            ("🏊", "Infinity Pool", "Kolam renang panorama"),
        ],
        "rooms": [
            ("Deluxe Ocean View", "35m²", "Rp 1.800.000", "Rp 2.500.000", "Popular"),
            ("Premium Suite", "55m²", "Rp 3.500.000", "", "Luxury"),
            ("Family Room", "45m²", "Rp 2.200.000", "", ""),
            ("Presidential Villa", "120m²", "Rp 8.000.000", "Rp 12.000.000", "Exclusive"),
        ],
        "testimonials": [
            ("\"Liburan terbaik yang pernah saya alami! Pelayanan prima dan pemandangan menakjubkan.\"", "— Keluarga Wijaya"),
            ("\"Spa nya luar biasa! Setelah sehari beraktivitas, terasa segar kembali.\"", "— Ibu Sinta"),
            ("\"Fine dining nya amazing! Chefs nya kreatif dan bahan-bahannya premium.\"", "— Pak Andi"),
        ],
        "footer_links": ["Kamar", "Restoran", "Spa", "Acara"],
        "help_links": ["Cara Booking", "Check-in/out", "Fasilitas", "FAQ"],
    },
    "hukum-pratama": {
        "name": "Pratama & Rekan",
        "tagline": "Firma Hukum Jakarta",
        "desc": "Firma hukum profesional di Jakarta dengan pengalaman lebih dari 15 tahun di bidang hukum bisnis dan corporate.",
        "bg": "#ffffff", "surface": "#fff", "text": "#333", "muted": "#666",
        "accent": "#1E3A5F", "accent2": "#2A4F7A", "gold": "#C8A951", "green": "#10b981",
        "hero_bg": "linear-gradient(135deg, #0f172a 0%, #1e3a5f 50%, #172554 100%)",
        "hero_gradient": "radial-gradient(circle at 30% 50%, rgba(30,58,95,.2), transparent 50%), radial-gradient(circle at 70% 40%, rgba(200,169,81,.08), transparent 50%)",
        "hero_accent_grad": "linear-gradient(90deg, #C8A951, #1E3A5F)",
        "font_heading": "'Inter', sans-serif",
        "font_body": "'Inter', system-ui, sans-serif",
        "features": [
            ("⚖️", "15+ Years Exp", "Pengalaman hukum panjang"),
            ("🏢", "Corporate Law", "Hukum korporasi"),
            ("👥", "Expert Team", "Tim profesional"),
            ("🛡️", "Client Focused", "Prioritas klien"),
        ],
        "services": [
            ("Hukum Korporasi", "Pendirian PT, M&A, kontrak", "", "", "Core", "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=400&q=80"),
            ("Hukum Perdata", "Sengketa, waris, tanah", "", "", "Popular", "https://images.unsplash.com/photo-1521791055366-0d553872125f?w=400&q=80"),
            ("Hukum Pidana", "Tindak pidana korporasi", "", "", "", "https://images.unsplash.com/photo-1589998059171-988d887df646?w=400&q=80"),
            ("Hukum Intelektual", "Merek, hak cipta, paten", "", "", "Specialty", "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=400&q=80"),
        ],
        "testimonials": [
            ("\"Firma hukum yang sangat profesional. Kasus perusahaan kami selesai dengan hasil memuaskan.\"", "— Direktur PT Maju Bersama"),
            ("\"Konsultasi hukum nya detail dan solutif. Harga juga transparan.\"", "— Bapak Hadi, Pengusaha"),
            ("\"Team nya responsif dan komunikatif. Update berkala tentang perkembangan kasus.\"", "— Ibu Rina, Startup Founder"),
        ],
        "footer_links": ["Korporasi", "Perdata", "Pidana", "Intelektual"],
        "help_links": ["Konsultasi", "Biaya", "Tim", "FAQ"],
    },
    "yayasan-harapan": {
        "name": "Yayasan Harapan Bangsa",
        "tagline": "Menyatukan Hati untuk Nusantara",
        "desc": "Yayasan nirlaba yang fokus pada pendidikan, kesehatan, dan pemberdayaan masyarakat Indonesia.",
        "bg": "#ffffff", "surface": "#fff", "text": "#1a1a2e", "muted": "#64748B",
        "accent": "#059669", "accent2": "#10b981", "gold": "#f59e0b", "green": "#10b981",
        "hero_bg": "linear-gradient(135deg, #064e3b 0%, #065f46 50%, #047857 100%)",
        "hero_gradient": "radial-gradient(circle at 30% 50%, rgba(5,150,105,.15), transparent 50%), radial-gradient(circle at 70% 40%, rgba(245,158,11,.1), transparent 50%)",
        "hero_accent_grad": "linear-gradient(90deg, #059669, #f59e0b)",
        "font_heading": "'Inter', sans-serif",
        "font_body": "'Inter', system-ui, sans-serif",
        "features": [
            ("📚", "Beasiswa Pendidikan", "500+ penerima"),
            ("🏥", "Kesehatan Masyarakat", "Posyandu & klinik"),
            ("🌱", "Lingkungan", "Penghijauan & daur ulang"),
            ("🤝", "Pemberdayaan", "UMKM & wirausaha"),
        ],
        "programs": [
            ("Beasiswa SD-SMA", "Pendidikan", "500+ anak", "", "Aktif", "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=400&q=80"),
            ("Posyandu Desa", "Kesehatan", "20 desa", "", "Berkelanjutan", "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=400&q=80"),
            ("UMKM Digital", "Ekonomi", "300+ UMKM", "", "Berjalan", "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=400&q=80"),
            ("Penghijauan Pantai", "Lingkungan", "10.000 pohon", "", "Target 2026", "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?w=400&q=80"),
        ],
        "testimonials": [
            ("\"Yayasan ini benar-benar membantu anak-anak kurang mampu mendapatkan pendidikan.\"", "— Bapak Sutrisno, Kepala Desa"),
            ("\"Program beasiswa nya life-changing. Saya bisa kuliah berkat bantuan mereka.\"", "— Siti Aminah, Mahasiswi"),
            ("\"Posyandu nya rutin dan layanan nya lengkap. Masyarakat sangat terbantu.\"", "— Ibu Rohani, Kader Posyandu"),
        ],
        "footer_links": ["Program", "Donasi", "Relawan", "Laporan"],
        "help_links": ["Cara Donasi", "Volunteer", "Proposal", "FAQ"],
    },
}

MOTION_TEMPLATE = '''<!DOCTYPE html>
<html lang="id">
<head>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={ga4}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','{ga4}');</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{name} — {tagline}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family={heading_font_encoded}&family={body_font_encoded}&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth;scroll-padding-top:80px}}
a,button{{transition:all .2s ease}}
:is(a,button,input,select,textarea):focus-visible{{outline:2px solid var(--accent);outline-offset:2px;border-radius:4px}}
.sr-only{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}}
.skip-link{{position:absolute;top:-100%;left:16px;background:var(--accent);color:#fff;padding:12px 20px;border-radius:8px;z-index:200;font-weight:600;text-decoration:none;font-size:.85rem}}
.skip-link:focus{{top:16px}}
:root{{--bg:{bg};--surface:{surface};--card:{surface};--border:rgba(255,255,255,.08);--text:{text};--muted:{muted};--accent:{accent};--accent2:{accent2};--gold:{gold};--green:{green};--radius:16px;--shadow:0 8px 32px rgba(0,0,0,.12)}}
body{{font-family:{font_body};background:var(--bg);color:var(--text);line-height:1.6;overflow-x:hidden}}
h1,h2,h3{{font-family:{font_heading};line-height:1.2}}
.container{{max-width:1200px;margin:0 auto;padding:0 24px}}

/* CUSTOM CURSOR */
.cursor-dot,.cursor-ring{{position:fixed;top:0;left:0;border-radius:50%;pointer-events:none;z-index:99999;mix-blend-mode:difference;display:none}}
.cursor-dot{{width:8px;height:8px;background:#fff;transform:translate(-50%,-50%)}}
.cursor-ring{{width:40px;height:40px;border:1.5px solid rgba(255,255,255,.5);transform:translate(-50%,-50%);transition:width .2s,height .2s,border-color .2s}}
@media(hover:hover){{.cursor-dot,.cursor-ring{{display:block}}}}

/* NAV */
nav{{position:sticky;top:0;z-index:1000;background:rgba(15,23,42,.92);backdrop-filter:blur(16px);border-bottom:1px solid rgba(255,255,255,.06);padding:0;transition:box-shadow .3s}}
nav.scrolled{{box-shadow:0 4px 30px rgba(0,0,0,.3)}}
.nav-inner{{max-width:1200px;margin:0 auto;padding:0 24px;display:flex;align-items:center;justify-content:space-between;height:72px}}
.nav-logo{{font-weight:800;font-size:1.3rem;color:#fff;display:flex;align-items:center;gap:10px;font-family:{font_heading}}}
.nav-logo span{{background:{hero_accent_grad};-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.nav-links{{display:flex;gap:32px;align-items:center;list-style:none}}
.nav-links a{{color:rgba(255,255,255,.7);text-decoration:none;font-size:.85rem;font-weight:500;letter-spacing:.02em;transition:color .2s;position:relative}}
.nav-links a::after{{content:'';position:absolute;bottom:-4px;left:0;width:0;height:2px;background:{hero_accent_grad};transition:width .3s}}
.nav-links a:hover{{color:#fff}}
.nav-links a:hover::after{{width:100%}}
.nav-cta{{background:{hero_accent_grad};color:#fff;padding:10px 24px;border-radius:999px;text-decoration:none;font-weight:600;font-size:.85rem;box-shadow:0 4px 16px rgba(59,130,246,.3);transition:all .25s}}
.nav-cta:hover{{transform:translateY(-2px);box-shadow:0 8px 24px rgba(59,130,246,.4)}}
.back-link{{font-size:.8rem!important;color:rgba(255,255,255,.5)!important;letter-spacing:0!important}}
.back-link:hover{{color:rgba(255,255,255,.8)!important}}
.hamburger{{display:none;flex-direction:column;gap:5px;cursor:pointer;z-index:1001;background:none;border:none;padding:10px}}
.hamburger span{{width:24px;height:2px;background:#fff;border-radius:2px;transition:all .3s}}

/* HERO — Cinematic Liquid Glass */
.hero{{min-height:100vh;display:flex;align-items:center;position:relative;overflow:hidden;background:{hero_bg};padding:120px 0 80px}}
.hero::before{{content:'';position:absolute;inset:0;background:{hero_gradient};pointer-events:none}}
.hero::after{{content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:conic-gradient(from 0deg,transparent,rgba(59,130,246,.04),transparent,rgba(139,92,246,.04),transparent);animation:hero-spin 25s linear infinite;pointer-events:none}}
@keyframes hero-spin{{to{{transform:rotate(360deg)}}}}
.hero-content{{max-width:1200px;margin:0 auto;padding:0 24px;display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:center;position:relative;z-index:2;width:100%}}
.hero-text{{max-width:600px}}
.hero-badge{{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.05);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.1);border-radius:999px;padding:8px 20px;font-size:.8rem;color:rgba(255,255,255,.8);margin-bottom:24px;letter-spacing:.03em}}
.hero-badge .dot{{width:6px;height:6px;background:#10b981;border-radius:50%;animation:pulse 2s infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.4}}}}
.hero h1{{font-size:clamp(2.5rem,6vw,4.5rem);margin-bottom:24px;line-height:1.08;color:#fff;letter-spacing:-.02em}}
.hero h1 span{{background:{hero_accent_grad};-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;display:inline}}
.hero p{{font-size:1.15rem;color:rgba(255,255,255,.6);margin-bottom:40px;line-height:1.7;max-width:480px}}
.hero-btns{{display:flex;gap:16px;flex-wrap:wrap}}
.btn-primary{{background:{hero_accent_grad};color:#fff;padding:16px 40px;border-radius:999px;text-decoration:none;font-weight:600;font-size:.95rem;transition:all .3s;box-shadow:0 8px 32px rgba(59,130,246,.3);position:relative;overflow:hidden}}
.btn-primary::before{{content:'';position:absolute;inset:0;background:linear-gradient(135deg,transparent,rgba(255,255,255,.15));opacity:0;transition:opacity .3s}}
.btn-primary:hover{{transform:translateY(-3px) scale(1.02);box-shadow:0 12px 40px rgba(59,130,246,.45)}}
.btn-primary:hover::before{{opacity:1}}
.btn-primary:active{{transform:translateY(-1px) scale(.98)}}
.btn-outline{{border:2px solid rgba(255,255,255,.15);color:#fff;padding:14px 36px;border-radius:999px;text-decoration:none;font-weight:600;font-size:.95rem;transition:all .3s;backdrop-filter:blur(12px);background:rgba(255,255,255,.03)}}
.btn-outline:hover{{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.3);transform:translateY(-2px)}}
.btn-outline:active{{transform:translateY(0) scale(.97)}}
.hero-visual{{position:relative;height:500px;display:flex;align-items:center;justify-content:center}}
.hero-card{{background:rgba(255,255,255,.03);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,.08);border-radius:24px;padding:40px;width:100%;max-width:420px;transform:perspective(1000px) rotateY(-8deg) rotateX(4deg);transition:transform .6s cubic-bezier(.16,1,.3,1);box-shadow:0 32px 64px rgba(0,0,0,.3)}}
.hero-card:hover{{transform:perspective(1000px) rotateY(0deg) rotateX(0deg)}}
.hero-card-icon{{font-size:3rem;margin-bottom:16px}}
.hero-card h3{{font-size:1.4rem;color:#fff;margin-bottom:12px}}
.hero-card p{{color:rgba(255,255,255,.6);font-size:.9rem;line-height:1.6;margin-bottom:20px}}
.hero-card-metric{{display:flex;gap:24px}}
.hero-card-metric div{{text-align:center}}
.hero-card-metric .num{{font-size:1.5rem;font-weight:800;background:{hero_accent_grad};-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.hero-card-metric .lbl{{font-size:.75rem;color:rgba(255,255,255,.5);margin-top:4px}}

/* FLOATING ORBS */
.orb{{position:absolute;border-radius:50%;filter:blur(80px);pointer-events:none;opacity:.4}}
.orb-1{{width:400px;height:400px;background:rgba(59,130,246,.15);top:-100px;right:-100px;animation:float 8s ease-in-out infinite}}
.orb-2{{width:300px;height:300px;background:rgba(139,92,246,.12);bottom:-50px;left:-50px;animation:float 10s ease-in-out infinite reverse}}
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-30px)}}}}

/* SECTIONS */
.section{{padding:120px 0;position:relative}}
.section-title{{text-align:center;font-size:clamp(2rem,4vw,3rem);margin-bottom:16px;letter-spacing:-.02em}}
.section-title span{{background:{hero_accent_grad};-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.section-sub{{text-align:center;color:var(--muted);margin-bottom:64px;font-size:1.05rem;max-width:600px;margin-left:auto;margin-right:auto}}

/* FADE-UP + STAGGER */
.fade-up{{opacity:0;transform:translateY(40px);transition:opacity .8s cubic-bezier(.16,1,.3,1),transform .8s cubic-bezier(.16,1,.3,1)}}
.fade-up.visible{{opacity:1;transform:translateY(0)}}
.stagger-item{{opacity:0;transform:translateY(30px);transition:opacity .6s cubic-bezier(.16,1,.3,1),transform .6s cubic-bezier(.16,1,.3,1)}}
.stagger-item.visible{{opacity:1;transform:translateY(0)}}

/* CARDS */
.card-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:24px}}
.card{{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:var(--radius);overflow:hidden;transition:transform .4s cubic-bezier(.16,1,.3,1),box-shadow .4s,border-color .4s;position:relative}}
.card::before{{content:'';position:absolute;inset:0;background:linear-gradient(135deg,{hero_accent_grad});opacity:0;transition:opacity .4s;z-index:0}}
.card:hover{{transform:translateY(-8px) scale(1.01);box-shadow:0 24px 48px rgba(0,0,0,.2);border-color:rgba(255,255,255,.12)}}
.card:hover::before{{opacity:.03}}
.card-img{{height:220px;overflow:hidden;position:relative}}
.card-img img{{width:100%;height:100%;object-fit:cover;transition:transform .6s cubic-bezier(.16,1,.3,1)}}
.card:hover .card-img img{{transform:scale(1.08)}}
.card-body{{padding:28px;position:relative;z-index:1}}
.card-body h3{{font-size:1.2rem;margin-bottom:10px;color:#fff}}
.card-body p{{color:rgba(255,255,255,.55);font-size:.9rem;line-height:1.65;margin-bottom:16px}}
.card-meta{{display:flex;justify-content:space-between;align-items:center}}
.card-price{{font-weight:700;font-size:1.1rem;background:{hero_accent_grad};-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.card-badge{{position:absolute;top:16px;left:16px;background:{hero_accent_grad};color:#fff;padding:6px 14px;border-radius:999px;font-size:.75rem;font-weight:600;z-index:2}}
.card-btn{{width:44px;height:44px;border-radius:50%;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.1);color:#fff;cursor:pointer;font-size:1.1rem;transition:all .2s;display:flex;align-items:center;justify-content:center}}
.card-btn:hover{{background:{hero_accent_grad};border-color:transparent;transform:scale(1.1)}}

/* STATS */
.stats-row{{display:flex;gap:32px;justify-content:center;flex-wrap:wrap;margin-top:48px}}
.stat-item{{text-align:center;padding:24px}}
.stat-num{{font-size:2.5rem;font-weight:800;background:{hero_accent_grad};-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:8px}}
.stat-lbl{{font-size:.85rem;color:rgba(255,255,255,.5)}}

/* TESTIMONIALS */
.testi-card{{background:rgba(255,255,255,.03);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.06);border-radius:var(--radius);padding:32px;transition:all .4s}}
.testi-card:hover{{transform:translateY(-6px);border-color:rgba(255,255,255,.12);box-shadow:0 20px 40px rgba(0,0,0,.15)}}
.testi-card p{{color:rgba(255,255,255,.65);font-style:italic;margin-bottom:20px;line-height:1.7;font-size:.95rem}}
.testi-author{{font-weight:600;color:#fff;font-size:.9rem}}
.testi-role{{font-size:.8rem;color:rgba(255,255,255,.4);margin-top:4px}}

/* CTA */
.cta-section{{text-align:center;padding:120px 0;background:linear-gradient(135deg,rgba(59,130,246,.05),rgba(139,92,246,.05))}}
.cta-section h2{{font-size:clamp(2rem,4vw,3rem);margin-bottom:20px}}
.cta-section p{{color:var(--muted);margin-bottom:40px;font-size:1.1rem;max-width:500px;margin-left:auto;margin-right:auto}}
.btn-wa{{display:inline-flex;align-items:center;gap:10px;background:#25d366;color:#fff;padding:16px 40px;border-radius:999px;text-decoration:none;font-weight:600;font-size:1rem;transition:all .3s;box-shadow:0 8px 24px rgba(37,211,102,.3)}}
.btn-wa:hover{{transform:translateY(-3px) scale(1.03);box-shadow:0 12px 32px rgba(37,211,102,.4)}}
.btn-wa:active{{transform:translateY(-1px) scale(.98)}}

/* FOOTER */
footer{{background:rgba(0,0,0,.3);border-top:1px solid rgba(255,255,255,.06);padding:64px 0 32px}}
.footer-grid{{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:40px;margin-bottom:40px}}
.footer-col h4{{font-family:{font_heading};font-size:1.1rem;margin-bottom:20px;color:#fff}}
.footer-col p,.footer-col a{{font-size:.85rem;color:rgba(255,255,255,.45);text-decoration:none;display:block;margin-bottom:10px;transition:color .2s;line-height:1.6}}
.footer-col a:hover{{color:#fff}}
.footer-bottom{{text-align:center;padding-top:32px;border-top:1px solid rgba(255,255,255,.06);font-size:.8rem;color:rgba(255,255,255,.3)}}
.footer-brand{{font-weight:700;font-size:1.1rem;background:{hero_accent_grad};-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:12px;display:block}}

/* HAMBURGER */
.hamburger{{display:none;background:none;border:none;cursor:pointer;padding:10px;z-index:1001;min-height:44px;min-width:44px}}
.hamburger span{{display:block;width:22px;height:2px;background:#fff;margin:5px 0;border-radius:2px;transition:all .3s}}
.hamburger.active span:nth-child(1){{transform:rotate(45deg) translate(5px,5px)}}
.hamburger.active span:nth-child(2){{opacity:0}}
.hamburger.active span:nth-child(3){{transform:rotate(-45deg) translate(5px,-5px)}}

/* MOBILE */
@media(max-width:768px){{
  .hamburger{{display:flex}}
  .nav-links{{display:none;position:fixed;top:0;right:-100%;width:75%;height:100vh;background:rgba(15,23,42,.98);backdrop-filter:blur(20px);flex-direction:column;justify-content:center;gap:32px;transition:right .4s cubic-bezier(.16,1,.3,1);padding:40px}}
  .nav-links.active{{display:flex;right:0}}
  .nav-links a{{font-size:1.1rem}}
  .hero-content{{grid-template-columns:1fr;text-align:center;gap:40px}}
  .hero-text{{max-width:100%}}
  .hero-visual{{display:none}}
  .hero-btns{{justify-content:center}}
  .hero p{{margin-left:auto;margin-right:auto}}
  .section{{padding:80px 0}}
  .card-grid{{grid-template-columns:1fr}}
  .footer-grid{{grid-template-columns:1fr 1fr}}
  .stats-row{{gap:16px}}
  input[type="text"],input[type="email"],textarea{{font-size:16px!important}}
}}
@media(max-width:428px){{
  .hero{{padding:80px 0 60px}}
  .hero h1{{font-size:2rem}}
  .section-title{{font-size:1.6rem}}
  .footer-grid{{grid-template-columns:1fr}}
  .stats-row{{flex-direction:column;align-items:center}}
}}

/* REDUCED MOTION */
@media(prefers-reduced-motion:reduce){{
  *,*::before,*::after{{animation-duration:.01ms!important;transition-duration:.01ms!important;scroll-behavior:auto!important}}
  .fade-up,.stagger-item{{opacity:1!important;transform:none!important}}
}}

/* SCROLL PROGRESS */
#scroll-progress{{position:fixed;top:0;left:0;height:3px;background:{hero_accent_grad};z-index:10001;transform-origin:left;transform:scaleX(0);width:100%;pointer-events:none}}
</style>
</head>
<body>
<div id="scroll-progress"></div>
<div class="cursor-dot"></div>
<div class="cursor-ring"></div>
<a href="{portfolio_url}" style="position:fixed;top:16px;left:16px;z-index:999;background:rgba(0,0,0,.7);color:#fff;padding:10px 18px;border-radius:10px;font-size:.8rem;font-weight:600;text-decoration:none;backdrop-filter:blur(12px);transition:all .2s;border:1px solid rgba(255,255,255,.1)" onmouseover="this.style.background='rgba(0,0,0,.9)';this.style.transform='translateY(-2px)'" onmouseout="this.style.background='rgba(0,0,0,.7)';this.style.transform='translateY(0)'">← Portfolio</a>
<a href="#main" class="skip-link">Skip to content</a>

<nav>
<div class="nav-inner">
  <div class="nav-logo">{name} <span>{tagline.split(' ')[0]}</span></div>
  <button class="hamburger" aria-label="Toggle menu" aria-expanded="false"><span></span><span></span><span></span></button>
  <ul class="nav-links">
    <li><a href="#main">Beranda</a></li>
    <li><a href="#features">Fitur</a></li>
    <li><a href="#products">Produk</a></li>
    <li><a href="#testimonials">Ulasan</a></li>
    <li><a href="#kontak" class="nav-cta">Hubungi Kami</a></li>
  </ul>
</div>
</nav>

<section class="hero" id="main">
<div class="orb orb-1"></div>
<div class="orb orb-2"></div>
<div class="hero-content">
  <div class="hero-text fade-up">
    <div class="hero-badge"><span class="dot"></span> Tersedia Sekarang</div>
    <h1>{name} <span>{tagline}</span></h1>
    <p>{desc}</p>
    <div class="hero-btns">
      <a href="#products" class="btn-primary">Lihat Koleksi</a>
      <a href="#kontak" class="btn-outline">Konsultasi Gratis</a>
    </div>
  </div>
  <div class="hero-visual fade-up" style="transition-delay:.15s">
    <div class="hero-card">
      <div class="hero-card-icon">🏆</div>
      <h3>Premium Quality</h3>
      <p>Kualitas terbaik dengan harga kompetitif. Kepuasan Anda adalah prioritas kami.</p>
      <div class="hero-card-metric">
        <div><div class="num">500+</div><div class="lbl">Klien Puas</div></div>
        <div><div class="num">4.9</div><div class="lbl">Rating</div></div>
        <div><div class="num">15+</div><div class="lbl">Tahun</div></div>
      </div>
    </div>
  </div>
</div>
</section>

<section class="section" id="features">
<div class="container">
  <h2 class="section-title fade-up">Mengapa <span>Memilih Kami</span></h2>
  <p class="section-sub fade-up">Kami berkomitmen memberikan pengalaman terbaik untuk setiap pelanggan</p>
  <div class="card-grid">
    {feature_cards}
  </div>
</div>
</section>

<section class="section" id="products" style="background:rgba(0,0,0,.2)">
<div class="container">
  <h2 class="section-title fade-up">Koleksi <span>Terbaru</span></h2>
  <p class="section-sub fade-up">Pilihan premium yang kami rekomendasikan untuk Anda</p>
  <div class="card-grid">
    {product_cards}
  </div>
</div>
</section>

<section class="section" id="testimonials">
<div class="container">
  <h2 class="section-title fade-up">Apa Kata <span>Mereka</span></h2>
  <p class="section-sub fade-up">Testimoni dari klien yang telah merasakan layanan kami</p>
  <div class="card-grid">
    {testimonial_cards}
  </div>
</div>
</section>

<section class="cta-section" id="kontak">
<div class="container fade-up">
  <h2>Siap Memulai?</h2>
  <p>Hubungi kami sekarang untuk konsultasi gratis. Tim kami siap membantu Anda.</p>
  <a href="https://wa.me/{whatsapp}?text=Halo%2C%20saya%20mau%20konsultasi%20tentang%20{name_encoded}" class="btn-wa">💬 Chat WhatsApp</a>
</div>
</section>

<footer>
<div class="container">
  <div class="footer-grid">
    <div class="footer-col">
      <span class="footer-brand">{name}</span>
      <p>{desc}</p>
    </div>
    <div class="footer-col">
      <h4>Layanan</h4>
      {footer_links_html}
    </div>
    <div class="footer-col">
      <h4>Bantuan</h4>
      {help_links_html}
    </div>
    <div class="footer-col">
      <h4>Kontak</h4>
      <p>WhatsApp: +62 878 9729 9985</p>
      <p>info@{name_encoded.lower().replace(' ','').replace('&','').replace('-','')}.id</p>
      <p>Indonesia</p>
    </div>
  </div>
  <div class="footer-bottom">© 2026 {name}. Dibuat oleh <a href="{portfolio_url}" style="color:rgba(255,255,255,.4);text-decoration:none">LYID Web Development</a></div>
</div>
</footer>

<script>
// Hamburger
document.querySelector('.hamburger').addEventListener('click',function(){{
  this.classList.toggle('active');
  var n=document.querySelector('.nav-links');
  n.classList.toggle('active');
  this.setAttribute('aria-expanded',n.classList.contains('active'))
}});

// IntersectionObserver — fade-up + stagger
var fadeEls=document.querySelectorAll('.fade-up,.stagger-item');
fadeEls.forEach(function(el,i){{el.style.transitionDelay=(i%8)*.08+'s'}});
var io=new IntersectionObserver(function(e){{e.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('visible');io.unobserve(e.target)}}}})}},{{threshold:0.1,rootMargin:'-50px 0px'}});
fadeEls.forEach(function(el){{io.observe(el)}});

// Mobile fallback — force visible after 3s
setTimeout(function(){{fadeEls.forEach(function(el){{el.classList.add('visible')}})}},3000);

// Scroll progress
window.addEventListener('scroll',function(){{
  var h=document.documentElement.scrollHeight-window.innerHeight;
  var pb=document.getElementById('scroll-progress');
  if(pb&&h>0)pb.style.transform='scaleX('+window.scrollY/h+')'
}},{{passive:true}});

// Nav scroll shadow
window.addEventListener('scroll',function(){{
  document.querySelector('nav').classList.toggle('scrolled',window.scrollY>50)
}},{{passive:true}});

// Custom cursor
var dot=document.querySelector('.cursor-dot'),ring=document.querySelector('.cursor-ring');
document.addEventListener('mousemove',function(e){{
  dot.style.left=e.clientX+'px';dot.style.top=e.clientY+'px';
  ring.style.left=e.clientX+'px';ring.style.top=e.clientY+'px'
}});
document.querySelectorAll('a,button,.card').forEach(function(el){{
  el.addEventListener('mouseenter',function(){{ring.style.width='60px';ring.style.height='60px';ring.style.borderColor='rgba(59,130,246,.6)'}});
  el.addEventListener('mouseleave',function(){{ring.style.width='40px';ring.style.height='40px';ring.style.borderColor='rgba(255,255,255,.5)'}});
}});

// iOS fix — ensure visibility
document.querySelectorAll('section,.hero,.card,.fade-up').forEach(function(el,i){{el.style.opacity='1';el.style.transform='none'}});
</script>
</body>
</html>'''

def slugify(name):
    return name.lower().replace(' ', '-').replace('&', '').replace("'", '')

def build_feature_cards(features):
    return '\n    '.join([
        f'''<div class="card stagger-item">
          <div class="card-body">
            <div style="font-size:2.5rem;margin-bottom:16px">{icon}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
          </div>
        </div>'''
        for icon, title, desc in features
    ])

def build_product_cards(products):
    cards = []
    for item in products:
        if len(item) == 5:
            name, meta, price, old_price, badge = item
            img = ""
        else:
            name, meta, price, old_price, badge, img = item
        badge_html = f'<span class="card-badge">{badge}</span>' if badge else ''
        old_price_html = f'<span style="font-size:.8rem;color:rgba(255,255,255,.35);text-decoration:line-through;margin-left:8px">{old_price}</span>' if old_price else ''
        img_html = f'<img src="{img}" alt="{name}" style="width:100%;height:100%;object-fit:cover" loading="lazy">' if img else ''
        cards.append(f'''<div class="card stagger-item">
          <div class="card-img">{badge_html}{img_html}<button class="card-btn" style="position:absolute;top:16px;right:16px">♡</button></div>
          <div class="card-body">
            <h3>{name}</h3>
            <p>{meta}</p>
            <div class="card-meta">
              <div class="card-price">{price}{old_price_html}</div>
              <button class="card-btn" style="width:auto;border-radius:999px;padding:0 20px;font-size:.85rem;font-weight:600">+</button>
            </div>
          </div>
        </div>''')
    return '\n    '.join(cards)

def build_testimonial_cards(testimonials):
    return '\n    '.join([
        f'''<div class="testi-card stagger-item">
          <p>{text}</p>
          <div class="testi-author">{author}</div>
        </div>'''
        for text, author in testimonials
    ])

def build_footer_links(links):
    return '\n      '.join([f'<a href="#">{l}</a>' for l in links])

def font_encoded(font):
    return font.replace("'", "").replace(" ", "+")

for site_id, cfg in CONFIGS.items():
    name_encoded = slugify(cfg["name"])
    heading_font_encoded = font_encoded(cfg["font_heading"].split("'")[1] if "'" in cfg["font_heading"] else cfg["font_heading"].replace("'", ""))
    body_font_encoded = font_encoded(cfg["font_body"].split("'")[1] if "'" in cfg["font_body"] else cfg["font_body"].replace("'", ""))

    html = MOTION_TEMPLATE
    html = html.replace("{ga4}", GA4)
    html = html.replace("{name}", cfg["name"])
    html = html.replace("{tagline}", cfg["tagline"])
    html = html.replace("{desc}", cfg["desc"])
    html = html.replace("{bg}", cfg["bg"])
    html = html.replace("{surface}", cfg["surface"])
    html = html.replace("{text}", cfg["text"])
    html = html.replace("{muted}", cfg["muted"])
    html = html.replace("{accent}", cfg["accent"])
    html = html.replace("{accent2}", cfg["accent2"])
    html = html.replace("{gold}", cfg["gold"])
    html = html.replace("{green}", cfg["green"])
    html = html.replace("{hero_bg}", cfg["hero_bg"])
    html = html.replace("{hero_gradient}", cfg["hero_gradient"])
    html = html.replace("{hero_accent_grad}", cfg["hero_accent_grad"])
    html = html.replace("{font_heading}", cfg["font_heading"])
    html = html.replace("{font_body}", cfg["font_body"])
    html = html.replace("{heading_font_encoded}", heading_font_encoded)
    html = html.replace("{body_font_encoded}", body_font_encoded)
    html = html.replace("{feature_cards}", build_feature_cards(cfg["features"]))
    product_source = cfg.get("products", cfg.get("courses", cfg.get("rooms", cfg.get("services", cfg.get("programs", [])))))
    html = html.replace("{product_cards}", build_product_cards(product_source))
    html = html.replace("{testimonial_cards}", build_testimonial_cards(cfg["testimonials"]))
    html = html.replace("{whatsapp}", WHATSAPP)
    html = html.replace("{name_encoded}", name_encoded)
    html = html.replace("{name_encoded.lower().replace(' ','').replace('&','').replace('-','')}.id", name_encoded + ".id")
    # Fix nav logo span placeholder — replace literal JS expression with first word of tagline
    tagline_first_word = cfg["tagline"].split(" ")[0]
    html = html.replace("{tagline.split(' ')[0]}", tagline_first_word)
    html = html.replace("{portfolio_url}", PORTFOLIO_URL)
    html = html.replace("{footer_links_html}", build_footer_links(cfg["footer_links"]))
    html = html.replace("{help_links_html}", build_footer_links(cfg["help_links"]))

    # Determine output path
    if site_id == "04-toko-online":
        out_path = os.path.join(SITES_DIR, "04-toko-online.html")
    else:
        out_path = os.path.join(SITES_DIR, site_id, "index.html")

    # For multi-file sites, also update style.css if exists
    css_path = os.path.join(SITES_DIR, site_id, "style.css")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ {out_path}")

    # Remove extra pages for multi-file sites (consolidate to single index.html)
    if site_id != "04-toko-online":
        for extra in ["kontak.html", "layanan.html", "tentang.html", "fasilitas.html", "kamar.html", "program.html", "properti.html"]:
            extra_path = os.path.join(SITES_DIR, site_id, extra)
            if os.path.exists(extra_path):
                os.remove(extra_path)
                print(f"  removed {extra}")
        if os.path.exists(css_path):
            os.remove(css_path)
            print(f"  removed style.css (consolidated to index.html)")
        # Remove audit files
        for audit in ["UI-AUDIT.md", "UX-AUDIT.md"]:
            audit_path = os.path.join(SITES_DIR, site_id, audit)
            if os.path.exists(audit_path):
                os.remove(audit_path)
                print(f"  removed {audit}")

print("\nDone. All 6 sites upgraded to MotionSites premium cinematic design.")
