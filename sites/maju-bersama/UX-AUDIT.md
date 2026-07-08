# UX Audit Report — PT Maju Bersama Website
**Date:** 2026-07-04
**Auditor:** UX Architect (Hermes Agent)
**Scope:** Responsive design, mobile layout, touch targets, typography

---

## Summary

Applied **P1 (critical)** and **P2 (important)** fixes to `style.css`. All 6 HTML pages inherit fixes via shared stylesheet. No HTML edits needed — inline style overrides handled via CSS attribute selector.

---

## Issues Found & Fixes Applied

### P1 — MUST FIX (applied)

| # | Issue | Fix |
|---|-------|-----|
| 1 | **Nav "Hubungi Kami" button visible on mobile** — appears alongside hamburger, wastes space, may overflow on 375px | `.nav-cta{display:none}` at ≤768px. Users access WhatsApp via floating button + CTA sections |
| 2 | **Form input font-size < 16px** — iOS Safari auto-zooms on inputs with font-size < 16px | Changed `font-size:.95rem` → `font-size:16px` on all inputs/textareas/selects |
| 3 | **Inline grid-template-columns don't collapse** — Hero grid (index.html), Visi/Misi grid (tentang.html), Brand grid (produk.html, 5-col) all use inline styles that override CSS | Added `[style*="grid-template-columns"]{grid-template-columns:1fr!important}` at ≤768px |
| 4 | **Hero h1 too large on mobile** — 3.2rem (~51px) overflows on 375px | Scaled to 1.8rem at 768px, 1.5rem at 428px |

### P2 — SHOULD FIX (applied)

| # | Issue | Fix |
|---|-------|-----|
| 5 | **Section padding too generous on mobile** — 100px → 60px still large | Reduced to 48px at ≤768px |
| 6 | **Typography too large on mobile** — section titles 1.7rem, CTA h2 2.2rem | Reduced to 1.5rem (768px), 1.3rem (428px) |
| 7 | **WA float button slightly large on mobile** — 60px OK but can be tighter | Reduced to 52px at ≤768px, adjusted positioning to 16px from edge |
| 8 | **Container padding too wide on mobile** — 24px eats into 375px viewport | Reduced to 16px (768px), 12px nav-inner (428px) |
| 9 | **Contact form padding too large on mobile** — 36px padding | Reduced to 24px at ≤768px |
| 10 | **Product/gallery image heights excessive on mobile** — 220px/260px | Reduced to 180px/200px |
| 11 | **Detail images too tall on mobile** — 350px | Reduced to 240px |
| 12 | **Contact map too tall on mobile** — 300px | Reduced to 200px |
| 13 | **Footer links need touch-target spacing** — tight together on mobile | Added padding to footer columns and links |
| 14 | **About features grid doesn't collapse** — 2-col on mobile | Forced to 1-col at ≤768px |
| 15 | **Section header margin too large** — 60px | Reduced to 40px at ≤768px |
| 16 | **Button sizing on small phones (≤428px)** — standard .btn padding still generous | Reduced padding/font-size at 428px breakpoint |

### PASS — No Fix Needed

| # | Check | Status |
|---|-------|--------|
| ✅ | Hamburger menu exists on all 6 pages | Present with toggle JS |
| ✅ | Hamburger has aria-label="Menu" | ✅ Accessible |
| ✅ | Nav links close on click | JS handler present |
| ✅ | WA float button ≥ 44px touch target | 52px on mobile, 60px on desktop |
| ✅ | All grids collapse to 1-col at 768px | CSS + inline override |
| ✅ | Images use loading="lazy" | All Unsplash images |
| ✅ | Images use object-fit:cover | Proper aspect ratios |
| ✅ | Viewport meta tag set | All pages |
| ✅ | Footer collapses to single column | ✅ |
| ✅ | Form row collapses to single column | ✅ |

---

## Breakpoint Strategy

| Breakpoint | Target |
|-----------|--------|
| ≤1024px | Tablet — grids go 2-col, footer 2-col, timeline linearizes |
| ≤768px | Mobile — all grids 1-col, nav hamburger, hide nav-cta, reduce spacing |
| ≤428px | Small phone — tighter typography, smaller buttons |

---

## Files Modified

- `style.css` — All responsive fixes in shared stylesheet (affects all 6 pages)

## Files NOT Modified (no changes needed)

- `index.html`, `tentang.html`, `layanan.html`, `produk.html`, `galeri.html`, `kontak.html`
