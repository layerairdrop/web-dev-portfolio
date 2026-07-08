# UX Audit — Web Dev Portfolio Sites
**Date:** 2026-07-03
**Auditor:** UX Architect (automated)
**Scope:** Responsive design, layout, accessibility across 7 demo sites

---

## Summary of Changes Applied

### P1 Critical (Applied ✅)

| # | Issue | Sites | Fix |
|---|-------|-------|-----|
| 1 | **No mobile navigation** — nav links hidden at 768px with no alternative | All 7 | Added hamburger menu button + CSS + JS toggle with aria-expanded |
| 2 | **Touch targets < 44px** — `.product-wishlist` and `.btn-cart` were 36×36px | 04-toko-online | Bumped to 44×44px |
| 3 | **Form input zoom on iOS** — `font-size: .9rem` (< 16px) triggers auto-zoom | 06-klinik | Added `font-size: 16px` in 428px media query |
| 4 | **focus-visible missing on form elements** — only `a`/`button` had focus styles | All 7 | Extended to `:is(a,button,input,select,textarea):focus-visible` |

### P2 Important (Applied ✅)

| # | Issue | Sites | Fix |
|---|-------|-------|-----|
| 5 | **No scroll-padding-top** — sticky/fixed nav overlaps section anchors | All 7 | Added `scroll-padding-top: 80px` to `html` rule |
| 6 | **No small phone breakpoint** — only 768px existed, 375/428px ignored | All 7 | Added `@media(max-width:428px)` with reduced padding, font sizes, single-column grids |
| 7 | **Footer 4-col grid** — still 2-col at 768px, too cramped at 375px | 04, 06, 07 | Added `grid-template-columns:1fr` in 428px query |
| 8 | **Dashboard preview overflow** — stats 4-col grid overflows small screens | 05-crypto | Added `grid-template-columns:1fr` + reduced padding in 428px query |

### P3 Nice-to-Have (Noted, not applied)

| # | Issue | Sites | Recommendation |
|---|-------|-------|----------------|
| 9 | No `clamp()` for body text | 01, 04 | Use `font-size: clamp(0.95rem, 2vw, 1.05rem)` for hero paragraphs |
| 10 | Marquee animation not paused on reduced-motion | 03-creative | Add `@media(prefers-reduced-motion:reduce){.marquee-track{animation:none}}` |
| 11 | No `loading="eager"` above-fold images explicit | 01, 02, 05 | Hero images already use emoji placeholders; low impact |
| 12 | Footer links not semantic `<nav>` | All 7 | Wrap footer link columns in `<nav aria-label="Footer">` |
| 13 | No skip-to-content link | All 7 | Add `<a href="#main" class="skip-link">Skip to content</a>` |
| 14 | No `prefers-color-scheme` support | All 7 | Consider dark mode toggle or auto-detection |
| 15 | Testimonial cards on 03 use scroll-snap but no keyboard nav | 03-creative | Add `tabindex="0"` to scrollable container |

---

## Per-Site Detail

### 01-restoran.html (Sajiku Kitchen)
**Changes:** hamburger menu, scroll-padding-top, focus-visible extension, 428px breakpoint, menu-grid/testi-grid collapse

**Remaining issues:**
- `.btn-wa` padding `10px 20px` yields ~38px height (close to 44px but not exact) — P3
- Contact form inputs have no `<label>` elements — P3 (a11y)
- No `name` attribute on form inputs — P3

### 02-startup.html (NexaFlow)
**Changes:** hamburger menu, scroll-padding-top, focus-visible extension, 428px breakpoint, stats-bar single-column

**Remaining issues:**
- `.btn-ghost` has no visible border on dark bg, hard to see — P3
- Logo row items too small for touch on mobile — P3

### 03-creative-agency.html (Kreasi Studio)
**Changes:** hamburger menu, scroll-padding-top, focus-visible extension (--pink), 428px breakpoint, serv-grid collapse

**Remaining issues:**
- Fixed nav with no background on desktop — content scrolls behind, may confuse — P3
- `.testi-wrap` horizontal scroll not keyboard-accessible — P3
- No `@media(prefers-reduced-motion)` for marquee animation — P3

### 04-toko-online.html (Batik Nusantara)
**Changes:** hamburger menu, scroll-padding-top, focus-visible extension, 428px breakpoint, touch targets 36→44px, product-grid/footer-grid collapse

**Remaining issues:**
- `.nav-icon` (🔍👤🛒) touch targets still small — add `min-height:44px;min-width:44px` — P3
- Tab buttons (`.tab`) padding `8px 20px` may be under 44px height — P3

### 05-crypto-web3.html (ChainVault)
**Changes:** hamburger menu, scroll-padding-top, focus-visible extension (--blue), 428px breakpoint, dash-stats single-column, dash-preview reduced padding

**Remaining issues:**
- `.dash-chips` (7D/30D/90D/1Y) very small on mobile — P3
- `.proto-dot` + text inline items wrap awkwardly on 375px — P3

### 06-klinik.html (Klinik Sehat Sentosa)
**Changes:** hamburger menu, scroll-padding-top, focus-visible extension (--blue), 428px breakpoint, form input font-size 16px, info-bar/footer-grid collapse

**Remaining issues:**
- FAQ `.faq-q` tap target could be larger — currently `padding:16px 20px` (~52px) — OK
- `.doc-chip` items very small on mobile — P3
- Form `<label>` elements not connected via `for`/`id` — P3

### 07-wedding.html (Everafter Studio)
**Changes:** hamburger menu, scroll-padding-top, focus-visible extension (--rose), 428px breakpoint, stats-bar/footer-grid collapse

**Remaining issues:**
- Gallery grid items may be too small on 375px (1fr + 1fr = ~180px each) — P3
- `.hero-content` padding `80px 0` excessive on mobile — P3

---

## Breakpoints Used

| Breakpoint | Target | Applied |
|------------|--------|---------|
| 1024px | Tablet/small laptop | 07-wedding (hero font) |
| 768px | Tablet portrait | All 7 (nav, grids) |
| 428px | Large phone (iPhone Pro Max) | All 7 (new) |

## CSS Architecture Notes

- All sites use inline `<style>` — no external CSS files
- CSS custom properties (`:root` vars) used consistently per site
- No build step — all changes are in-place HTML edits
- `clamp()` used for hero headings (good), not for body text (P3)
- `object-fit: cover` used on images with inline styles (good)
- `loading="lazy"` on below-fold images (good)
