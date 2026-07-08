# UI AUDIT V2 — Second Pass Visual & Interactive Polish

**Date:** 2026-07-04  
**Scope:** All 10 HTML files in web-dev-portfolio  
**First pass added:** smooth scroll, transitions, focus-visible, fixed footer colors  
**UX Architect V2 added:** hamburger, form labels, skip-to-content, touch targets, aria

---

## 1. VISUAL CONSISTENCY

### 1.1 Cards — padding/radius/shadow INCONSISTENT

| File | Card Class | Padding | Radius | Shadow | Hover |
|------|-----------|---------|--------|--------|-------|
| index.html | `.port-card` | 20px body | 16px | none | translateY(-6px)+border+shadow ✅ |
| index.html | `.price-card` | 32px | 16px | none | border-color only ⚠️ no lift |
| index.html | `.process-card` | 24px | 16px | none | **NO hover** ❌ |
| 01-restoran | `.menu-card` | 20px | 12px | 0 4px 20px | translateY(-4px) ✅ |
| 01-restoran | `.testi-card` | 24px | 12px | 0 4px 20px | **NO hover** ❌ |
| 02-startup | `.feat-card` | 28px | 12px | none | border-color only ⚠️ |
| 02-startup | `.price-card` | 32px | 12px | none | border-color only ⚠️ |
| 03-agency | `.serv-card` | 32px | 16px | none | border-color only ⚠️ |
| 03-agency | `.testi-card` | 32px | 16px | none | **NO hover** ❌ |
| 04-toko | `.product-card` | 16px | 12px | 0 4px 16px | translateY(-4px)+shadow ✅ |
| 04-toko | `.testi-card` | 24px | 12px | none | **NO hover** ❌ |
| 05-crypto | `.feat-card` | 28px | 16px | none | border+translateY(-4px) ✅ |
| 05-crypto | `.price-card` | 32px | 16px | none | border-color only ⚠️ |
| 06-klinik | `.serv-card` | 24px | 16px | none | border+translateY(-4px)+shadow ✅ |
| 06-klinik | `.doc-card` | 0 | 16px | none | translateY(-4px) ✅ |
| 06-klinik | `.testi-card` | 24px | 16px | none | **NO hover** ❌ |
| 07-wedding | `.serv-card` | 24px | 16px | none | translateY(-4px)+shadow ✅ |
| 07-wedding | `.testi-card` | 28px | 16px | 0 4px 24px | **NO hover** ❌ |
| 07-wedding | `.pkg-card` | 32px | 16px | none | border+translateY(-4px)+shadow ✅ |

**Issues found:**
- ❌ **6 cards have NO hover effect** — process cards (index), all testi cards (restoran, agency, toko, klinik, wedding)
- ⚠️ **6 cards have border-color-only hover** — no lift, no shadow → feels flat
- ✅ 9 cards have proper hover interaction

### 1.2 Buttons — hover states INCONSISTENT

| Button | Files | Hover Effect |
|--------|-------|-------------|
| `.btn-primary` | index | translateY(-2px)+shadow ✅ |
| `.btn-primary` | restoran | background change only ⚠️ |
| `.btn-primary` | startup | opacity .85 ⚠️ |
| `.btn-primary` | agency | translateY(-2px)+shadow ✅ |
| `.btn-primary` | toko | background change ⚠️ |
| `.btn-primary` | crypto | translateY(-2px)+shadow ✅ |
| `.btn-primary` | klinik | translateY(-2px)+shadow ✅ |
| `.btn-primary` | wedding | translateY(-2px) ✅ |
| `.btn-cta` | index, agency | opacity .85 / scale(1.05) ⚠️ no lift |
| `.btn-ghost` | index, startup | border-color / color change ⚠️ |
| `.btn-wa` | restoran, toko, crypto | opacity .85 ⚠️ |
| `.btn-card` | index (filled) | **NO hover** ❌ |
| `.btn-card` | crypto (filled) | **NO hover** ❌ |
| `.btn-submit` | order | translateY(-2px)+shadow ✅ |
| `.btn-wa` | order | opacity .85 ⚠️ |

**Issues found:**
- ❌ `.btn-card.filled` in index.html and 05-crypto has **NO hover effect at all**
- ⚠️ Many CTA/nav buttons only use opacity hover — doesn't feel interactive

### 1.3 Section Titles

| File | Font-size | Weight | Letter-spacing | Alignment |
|------|----------|--------|----------------|-----------|
| index | 2rem | 700 | none | center ✅ |
| restoran | 2rem | serif default | none | center ✅ |
| startup | 2rem | 700 | none | center ✅ |
| agency | 2.5rem | 700 | none | left ⚠️ different |
| toko | 2rem | serif default | none | center ✅ |
| crypto | 2rem | 700 | none | center ✅ |
| klinik | 2rem | 800 | none | center ✅ |
| wedding | 2.2rem | 500 (serif) | none | center ✅ |

**Issues:**
- Agency `.section-title` is left-aligned + 2.5rem — intentional for its bold design
- Overall: reasonably consistent ✅

### 1.4 Form Inputs

| File | Padding | Radius | Font-size | Focus |
|------|---------|--------|-----------|-------|
| restoran | 12px 16px | 8px | 95rem/16px | border-color ⚠️ no ring |
| toko (nav search) | 8px 14px | 8px | .85rem | none ❌ |
| klinik | 10px 14px | 10px | .9rem | border+ring ✅ |
| wedding (RSVP) | 12px 16px | 10px | 16px | border-color via focus-visible only |
| order | 12px 16px | 10px | 16px | border+ring ✅ |

**Issues:**
- ⚠️ Restoran and wedding form inputs lack visible focus ring (rely only on `:focus-visible` outline)
- ❌ Toko search input has no focus styling

### 1.5 Color Consistency

Each site has its own color palette — this is **intentional** (different industries). No cross-site color inconsistency issues.

---

## 2. MICRO-INTERACTIONS

### 2.1 Missing Hover States (CRITICAL)
- ❌ `.process-card` in index.html — no hover at all
- ❌ `.testi-card` in restoran, agency, toko, klinik, wedding — no hover at all
- ❌ `.btn-card.filled` in index.html, crypto — no hover at all
- ❌ `.serv-card` in agency `.serv-card` only does border-color — needs lift

### 2.2 Missing Active/Pressed States
- **NO file** has `:active` state on buttons (e.g., `transform: translateY(0)` to snap back)
- Adding pressed feedback improves perceived responsiveness

### 2.3 Transition Coverage
- ✅ `a, button { transition: all .2s ease }` in all files
- ⚠️ Cards use inline `transition:` but some are missing `box-shadow` from transition list

### 2.4 Focus-Visible
- ✅ All files have `:focus-visible` with outline
- ✅ Consistent `outline-offset: 2px` across all

---

## 3. IMAGE QUALITY

### 3.1 Unsplash Images
All Unsplash URLs use `?w=XXX&q=80` format — should load correctly. No 404-risk detected (Unsplash serves any valid photo ID with resize params).

### 3.2 Aspect Ratios
- ✅ All images use `object-fit: cover` with explicit height containers
- ⚠️ Klinik hero-card icon has `height:80px` with `overflow:hidden` on a 4rem icon → may clip awkwardly

### 3.3 Loading
- ✅ All non-hero images have `loading="lazy"`
- ✅ Wedding hero has `loading="eager"` (correct for LCP)
- ⚠️ No `decoding="async"` on any images (minor perf)

---

## 4. TYPOGRAPHY

### 4.1 Heading Hierarchy
- ✅ Consistent h1 → h2 → h3 usage across all sites
- ✅ Each site uses 1-2 complementary fonts (serif + sans)

### 4.2 Line Heights
- ✅ Body: 1.6 (all files) — readable
- ✅ Wedding: 1.7 — slightly more spacious, appropriate for elegant theme
- ✅ Hero headings use 1.1-1.2 — tight but acceptable for impact

### 4.3 Letter Spacing on Uppercase
- ✅ `.section-label` has `letter-spacing: .1em-.2em` — consistent
- ⚠️ No issues found

### 4.4 Font Weights
- Consistent within each site ✅
- Index.html uses 900 for hero h1 while others use 800 — intentional bolder display

---

## 5. DARK THEME POLISH (index, 02-startup, 05-crypto, 03-agency, order)

### 5.1 Card vs Page Background
| File | bg | surface | card | Contrast |
|------|-----|---------|------|----------|
| index | #09090b | #111113 | #18181b | ✅ distinguishable |
| startup | #09090b | #111113 | #18181b | ✅ |
| agency | #0a0a0a | #141414 | #1c1c1c | ✅ |
| crypto | #09090b | #0f0f12 | #151518 | ✅ subtler, intentional |

### 5.2 Border Visibility
- All use `#27272a` or `#2a2a2a` — visible but subtle ✅

### 5.3 Text Contrast (WCAG AA)
- `#e4e4e7` on `#09090b` → ratio ~13.5:1 ✅ excellent
- `#71717a` (muted) on `#09090b` → ratio ~4.6:1 ✅ passes AA
- Agency `#888` (muted) on `#0a0a0a` → ratio ~4.2:1 ⚠️ borderline AA

### 5.4 Gradients
- ✅ All gradient accents use smooth multi-stop transitions

---

## 6. LIGHT THEME POLISH (restoran, toko, klinik, wedding)

### 6.1 Background Warmth
- Restoran: `#fffbf5` → warm ✅
- Toko: `#faf8f4` → warm ✅  
- Klinik: `#f8fafc` → cool, medical ✅
- Wedding: `#fdfbf9` → warm ✅

### 6.2 Shadows
- Restoran: `0 4px 20px rgba(0,0,0,.08)` ✅
- Toko: `0 4px 16px rgba(44,24,16,.08)` ✅
- Klinik: `0 4px 20px rgba(0,0,0,.06)` ✅
- Wedding: `0 4px 24px rgba(44,36,32,.08)` ✅

### 6.3 Text Contrast
- All light sites use dark text (#1a1a1a to #2c2420) on light backgrounds ✅ excellent contrast

---

## 7. INTERACTIVE ELEMENTS SUMMARY

### 7.1 Missing Hover Effects — MUST FIX (P1)
1. ❌ `.process-card` (index) — no hover
2. ❌ `.testi-card` (restoran) — no hover  
3. ❌ `.testi-card` (agency) — no hover
4. ❌ `.testi-card` (toko) — no hover
5. ❌ `.testi-card` (klinik) — no hover
6. ❌ `.testi-card` (wedding) — no hover
7. ❌ `.btn-card.filled` (index) — no hover
8. ❌ `.btn-card.filled` (crypto) — no hover
9. ❌ `.btn-card.primary` (startup) — no hover
10. ⚠️ `.serv-card` (agency) — only border, no lift
11. ⚠️ `.feat-card` (startup) — only border, no lift
12. ⚠️ `.price-card` (index, startup, crypto) — only border, no lift

### 7.2 Scroll Animations — MISSING (P1)
- **NO file** has Intersection Observer fade-in animations
- This is a major polish gap for a portfolio site

### 7.3 Image Loading Animation — MISSING (P1)
- No skeleton/pulse animation on image containers
- Emoji placeholders in index portfolio cards could have subtle pulse

---

## PRIORITY FIXES

### P1 (Apply Now)
1. Add Intersection Observer fade-in to all sections in all files
2. Add hover effects to ALL cards missing them
3. Add hover transform to ALL buttons missing it
4. Add `:active` states to buttons for pressed feedback
5. Ensure all cards have `translateY` + `box-shadow` hover

### P2 (Nice to Have)
6. Add `decoding="async"` to images
7. Add pulse animation to image placeholders
8. Make `.btn-card.filled` have gradient hover
