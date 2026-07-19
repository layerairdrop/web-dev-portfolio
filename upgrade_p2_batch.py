import os, re

sites_dir = r"C:\Users\raman\LYID-BOTS\web-dev-portfolio\sites"

all_files = []
for root, dirs, files in os.walk(sites_dir):
    for f in sorted(files):
        if f.endswith('.html'):
            rel = os.path.relpath(os.path.join(root, f), sites_dir)
            all_files.append(rel)

fixed = []

for rel in all_files:
    path = os.path.join(sites_dir, rel)
    with open(path, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    original = content
    
    # 1. ADD overflow-x protection
    if 'overflow-x' not in content.lower():
        # Add to * selector or body
        content = content.replace(
            '*{box-sizing:border-box;margin:0;padding:0}',
            '*{box-sizing:border-box;margin:0;padding:0;max-width:100vw;overflow-x:hidden}'
        )
        if content == original:
            # Try body selector
            content = content.replace(
                'body{',
                'body{overflow-x:hidden;'
            )
    
    # 2. ADD font-display swap to Google Fonts
    if 'font-display' not in content.lower():
        content = re.sub(
            r'(fonts\.googleapis\.com/css2\?[^"\']+)"',
            r'\1&display=swap"',
            content,
            flags=re.IGNORECASE
        )
    
    # 3. ADD robots meta
    if 'name="robots"' not in content.lower():
        # Insert after charset or viewport
        if '<meta name="viewport"' in content:
            content = content.replace(
                '<meta name="viewport"',
                '<meta name="robots" content="index, follow, max-image-preview:large">\n<meta name="viewport"'
            )
        elif '<meta charset' in content:
            content = content.replace(
                '<meta charset',
                '<meta name="robots" content="index, follow, max-image-preview:large">\n<meta charset'
            )
    
    # 4. ADD width/height to images (CLS fix)
    # Extract first Unsplash image dimensions or use defaults
    imgs = re.findall(r'<img[^>]+src="(https://images\.unsplash\.com/[^"]+)"[^>]*>', content)
    img_tags = re.findall(r'<img[^>]+>', content)
    
    for i, img_tag in enumerate(img_tags):
        if 'width=' in img_tag and 'height=' in img_tag:
            continue
        
        # Default dimensions
        width = '800'
        height = '600'
        
        # Try to extract from existing classes or context
        if 'hero' in img_tag.lower() or 'banner' in img_tag.lower():
            width = '1200'
            height = '600'
        elif 'card' in img_tag.lower() or 'menu' in img_tag.lower():
            width = '400'
            height = '300'
        elif 'gallery' in img_tag.lower() or 'galeri' in img_tag.lower():
            width = '600'
            height = '400'
        
        # Add width/height before closing >
        if 'width=' not in img_tag:
            new_tag = img_tag.replace('>', f' width="{width}" height="{height}" loading="lazy">', 1)
            content = content.replace(img_tag, new_tag, 1)
    
    # 5. ADD basic schema.org markup
    if 'schema.org' not in content.lower() and 'application/ld+json' not in content.lower():
        # Extract business name from title
        title_match = re.search(r'<title>(.*?)(?:\s*[|—–-]\s*).*?</title>', content)
        if not title_match:
            title_match = re.search(r'<title>(.*?)</title>', content)
        
        if title_match:
            name = title_match.group(1).strip()
            # Determine type
            if any(x in name.lower() for x in ['restoran', 'kitchen', 'cafe']):
                schema_type = 'Restaurant'
            elif any(x in name.lower() for x in ['startup', 'tech', 'digital']):
                schema_type = 'ProfessionalService'
            elif any(x in name.lower() for x in ['wedding', 'pernikahan']):
                schema_type = 'WeddingVenue'
            elif any(x in name.lower() for x in ['klinik', 'hospital', 'medical']):
                schema_type = 'MedicalBusiness'
            else:
                schema_type = 'LocalBusiness'
            
            schema_json = f"""\n<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "{schema_type}",
  "name": "{name}",
  "url": "https://ralies.biz.id/sites/{rel.replace(chr(92), '/')}",
  "description": "{name} - Dibuat oleh LYID Web Development"
}}
</script>"""
            
            # Insert before </head>
            content = content.replace('</head>', schema_json + '\n</head>', 1)
    
    # 6. ADD hreflang
    if 'hreflang' not in content.lower():
        # Insert after canonical or before </head>
        if '<link rel="canonical"' in content:
            content = content.replace(
                '<link rel="canonical"',
                '<link rel="alternate" hreflang="id" href="https://ralies.biz.id/sites/' + rel.replace(chr(92), '/') + '">\n<link rel="alternate" hreflang="en" href="https://ralies.biz.id/sites/' + rel.replace(chr(92), '/') + '">\n<link rel="canonical"'
            )
        else:
            content = content.replace('</head>', '<link rel="alternate" hreflang="id" href="https://ralies.biz.id/sites/' + rel.replace(chr(92), '/') + '">\n</head>', 1)
    
    if content != original:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(content)
        fixed.append(rel)

print(f"=== BATCH FIX COMPLETE ===\n")
print(f"Fixed {len(fixed)} files:")
for rel in fixed:
    print(f"  - {rel}")
