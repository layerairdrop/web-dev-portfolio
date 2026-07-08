#!/usr/bin/env python3
"""Auto-fix common audit issues across LYID portfolio sites."""
import os, re

SITES_DIR = os.path.expanduser("~/LYID-BOTS/web-dev-portfolio/sites")
SITES = [
    "01-restoran.html",
    "02-startup.html",
    "03-creative-agency.html",
    "04-toko-online.html",
    "05-crypto-web3.html",
    "06-klinik.html",
    "07-wedding.html",
    "08-company-profile-demo.html",
    "company/index.html",
    "company.html",
    "edu-academy/index.html",
    "grand-hotel/index.html",
    "hukum-pratama/index.html",
    "maju-bersama/index.html",
    "properti-premium/index.html",
    "yayasan-harapan/index.html",
]

OG_IMAGES = {
    "01-restoran.html": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1200&q=80",
    "02-startup.html": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&q=80",
    "03-creative-agency.html": "https://images.unsplash.com/photo-1558655146-9f40138edfeb?w=1200&q=80",
    "04-toko-online.html": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=1200&q=80",
    "05-crypto-web3.html": "https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=1200&q=80",
    "06-klinik.html": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=1200&q=80",
    "07-wedding.html": "https://images.unsplash.com/photo-1519741497674-611481863552?w=1200&q=80",
    "08-company-profile-demo.html": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1200&q=80",
    "company/index.html": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1200&q=80",
    "company.html": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1200&q=80",
    "edu-academy/index.html": "https://images.unsplash.com/photo-1501504905252-47347d3c7b43?w=1200&q=80",
    "grand-hotel/index.html": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=1200&q=80",
    "hukum-pratama/index.html": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=1200&q=80",
    "maju-bersama/index.html": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1200&q=80",
    "properti-premium/index.html": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1200&q=80",
    "yayasan-harapan/index.html": "https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?w=1200&q=80",
}

for site in SITES:
    path = os.path.join(SITES_DIR, site)
    if not os.path.exists(path):
        continue
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Add OG tags if missing
    if 'og:title' not in content:
        title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
        if title_match:
            title_text = title_match.group(1).strip()
            # Extract site name from title
            site_name = title_text.split('—')[0].split('-')[0].strip()
            og_img = OG_IMAGES.get(site, "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1200&q=80")
            og_url = f"https://ralies.biz.id/sites/{site.replace('/index.html', '')}"
            
            og_tags = f'<meta property="og:title" content="{title_text}">\n<meta property="og:description" content="{title_text}">\n<meta property="og:image" content="{og_img}">\n<meta property="og:url" content="{og_url}">\n<meta property="og:type" content="website">\n'
            content = content.replace('<title>', og_tags + '<title>')
            print(f"✓ Added OG tags: {site}")
    
    # 2. Add WhatsApp link if missing
    if 'wa.me' not in content:
        # Add to footer if exists
        if '<footer>' in content:
            content = content.replace(
                '</footer>',
                '<div style="text-align:center;padding:24px;background:rgba(37,211,102,.1);border-top:1px solid rgba(37,211,102,.2)">\n<a href="https://wa.me/6287897299985?text=Halo%2C%20saya%20mau%20konsultasi" style="display:inline-flex;align-items:center;gap:8px;background:#25d366;color:#fff;padding:12px 28px;border-radius:999px;text-decoration:none;font-weight:600;font-size:.9rem">💬 Chat WhatsApp</a>\n</div>\n</footer>'
            )
            print(f"✓ Added WhatsApp: {site}")
    
    # 3. Add GA4 if missing
    if 'G-C6BH106VBQ' not in content:
        ga4_script = '''<script async src="https://www.googletagmanager.com/gtag/js?id=G-C6BH106VBQ"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-C6BH106VBQ');</script>'''
        content = content.replace('</head>', ga4_script + '\n</head>')
        print(f"✓ Added GA4: {site}")
    
    # 4. Add LYID credit if missing
    if 'LYID Web Development' not in content and 'Dibuat oleh' not in content:
        if '</body>' in content:
            content = content.replace(
                '</body>',
                '<footer style="text-align:center;padding:24px;color:#666;font-size:.8rem;border-top:1px solid #eee">© 2026. Dibuat oleh <a href="https://ralies.biz.id" style="color:#3b82f6;text-decoration:none">LYID Web Development</a></footer>\n</body>'
            )
            print(f"✓ Added LYID credit: {site}")
    
    # 5. Add missing CSS patterns
    css_additions = []
    
    # Focus visible
    if ':focus-visible' not in content:
        css_additions.append(':is(a,button,input,select,textarea):focus-visible{outline:2px solid #3b82f6;outline-offset:2px;border-radius:4px}')
    
    # Smooth scroll
    if 'scroll-behavior:smooth' not in content:
        css_additions.append('html{scroll-behavior:smooth;scroll-padding-top:80px}')
    
    # 768px breakpoint
    if '@media(max-width:768px)' not in content:
        css_additions.append('@media(max-width:768px){.nav-links-m{display:none}.hamburger{display:block}.grid{grid-template-columns:1fr}}')
    
    # 428px breakpoint
    if '@media(max-width:428px)' not in content:
        css_additions.append('@media(max-width:428px){body{padding:20px 16px}.hero{padding:60px 0 40px}}')
    
    # Reduced motion
    if 'prefers-reduced-motion' not in content:
        css_additions.append('@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;transition-duration:.01ms!important;scroll-behavior:auto!important}}')
    
    # Skip link
    if 'skip-link' not in content:
        skip_link = '<a href="#main" class="skip-link" style="position:absolute;top:-100%;left:16px;background:#3b82f6;color:#fff;padding:12px 20px;border-radius:8px;z-index:200;font-weight:600;text-decoration:none;font-size:.85rem">Skip to content</a>'
        content = content.replace('<body>', '<body>\n' + skip_link)
        css_additions.append('.skip-link:focus{top:16px}')
    
    if css_additions:
        # Find </style> and inject before it
        if '</style>' in content:
            addition = '\n/* AUTO-FIXED */\n' + '\n'.join(css_additions) + '\n'
            content = content.replace('</style>', addition + '</style>', 1)
            print(f"✓ Added CSS fixes: {site}")
    
    # 6. Add hamburger JS if missing
    if 'hamburger' in content and 'addEventListener' not in content:
        hamburger_js = '''
<script>
const hamburger=document.getElementById('hamburger'),navLinks=document.getElementById('navLinksM');
if(hamburger){hamburger.addEventListener('click',()=>{hamburger.classList.toggle('active');navLinks.classList.toggle('active');hamburger.setAttribute('aria-expanded',navLinks.classList.contains('active'))})}
</script>'''
        content = content.replace('</body>', hamburger_js + '\n</body>')
        print(f"✓ Added hamburger JS: {site}")
    
    # Write back
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("\n=== Fix Complete ===")
print("Run audit_sites.py again to verify all issues resolved")
