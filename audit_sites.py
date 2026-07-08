#!/usr/bin/env python3
"""Automated audit of all LYID portfolio sites — checks HTML + linked CSS."""
import os, re

SITES_DIR = os.path.expanduser("~/LYID-BOTS/web-dev-portfolio/sites")
SITES = [
    ("01-restoran.html", None),
    ("02-startup.html", None),
    ("03-creative-agency.html", None),
    ("04-toko-online.html", None),
    ("05-crypto-web3.html", None),
    ("06-klinik.html", None),
    ("07-wedding.html", None),
    ("08-company-profile-demo.html", None),
    ("company/index.html", "company/style.css"),
    ("company.html", None),
    ("edu-academy/index.html", None),
    ("grand-hotel/index.html", None),
    ("hukum-pratama/index.html", None),
    ("maju-bersama/index.html", "maju-bersama/style.css"),
    ("properti-premium/index.html", None),
    ("yayasan-harapan/index.html", None),
]

def audit_file(html_path, css_path):
    issues = []
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    css = ""
    if css_path:
        full_css_path = os.path.join(SITES_DIR, css_path)
        if os.path.exists(full_css_path):
            with open(full_css_path, "r", encoding="utf-8") as f:
                css = f.read()
    
    combined = html + css
    
    # P1 Critical
    if '<!DOCTYPE html>' not in html:
        issues.append("P1: Missing DOCTYPE")
    if 'name="viewport"' not in html:
        issues.append("P1: Missing viewport meta")
    if 'hamburger' not in combined.lower():
        issues.append("P1: No hamburger menu for mobile")
    if 'aria-expanded' not in combined.lower():
        issues.append("P2: Missing aria-expanded on hamburger")
    
    # P2 Important
    if ':focus-visible' not in combined:
        issues.append("P2: Missing focus-visible styles")
    if 'scroll-behavior:smooth' not in combined:
        issues.append("P3: Missing smooth scroll")
    if '@media(max-width:768px)' not in combined:
        issues.append("P2: Missing 768px breakpoint")
    if '@media(max-width:428px)' not in combined:
        issues.append("P2: Missing 428px breakpoint")
    if 'prefers-reduced-motion' not in combined:
        issues.append("P3: Missing reduced-motion support")
    if 'skip-link' not in html.lower():
        issues.append("P3: Missing skip-to-content link")
    if 'og:title' not in html:
        issues.append("P2: Missing Open Graph tags")
    if 'G-C6BH106VBQ' not in html:
        issues.append("P2: Missing GA4 tracking")
    if 'wa.me' not in html:
        issues.append("P2: Missing WhatsApp link")
    if 'LYID Web Development' not in html and 'Dibuat oleh' not in html:
        issues.append("P3: Missing LYID credit")
    
    # Check images have alt
    imgs = re.findall(r'<img[^>]*>', html)
    missing_alt = [img for img in imgs if 'alt=' not in img]
    if missing_alt:
        issues.append(f"P2: {len(missing_alt)} images missing alt text")
    
    return issues

print("=== LYID Portfolio Sites Audit (HTML + CSS) ===\n")
all_issues = {}

for site, css_file in SITES:
    html_path = os.path.join(SITES_DIR, site)
    css_path = os.path.join(SITES_DIR, css_file) if css_file else None
    
    if not os.path.exists(html_path):
        print(f"SKIP: {site} (not found)")
        continue
    
    issues = audit_file(html_path, css_path)
    all_issues[site] = issues
    
    if issues:
        print(f"✗ {site} ({len(issues)} issues):")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print(f"✓ {site} — clean")

print("\n=== Summary ===")
total_issues = sum(len(v) for v in all_issues.values())
sites_with_issues = sum(1 for v in all_issues.values() if v)
print(f"Sites checked: {len([s for s,_ in SITES if os.path.exists(os.path.join(SITES_DIR, s))])}")
print(f"Sites with issues: {sites_with_issues}")
print(f"Total issues: {total_issues}")

if total_issues == 0:
    print("\n✓ All sites passed — ready for production deploy")
else:
    print("\n✗ Issues found")
