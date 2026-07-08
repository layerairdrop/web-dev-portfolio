# UI Design Audit — PT Maju Bersama

**Auditor**: UI Designer subagent  
**Date**: 2026-07-04  
**Scope**: 6 HTML pages + shared style.css

---

## Summary

Overall the design system is solid — CSS variables used consistently, card styles cohesive, spacing rhythm good. Found 3 P1 issues (fixed) and 6 P2 issues (noted).

---

## ✅ What's Good

| Area | Status |
|------|--------|
| **Color consistency** | ✅ All semantic colors use CSS variables (`--accent`, `--text`, `--bg`, etc.) |
| **Typography hierarchy** | ✅ Clear progression: page-hero h1 (2.8rem) → section-title (2.2rem) → card h3 (~1rem) |
| **Spacing rhythm** | ✅ Sections consistently use `padding:100px` desktop, `48px` mobile |
| **Card consistency** | ✅ All cards share `var(--radius)`, `var(--border)`, `var(--shadow)` |
| **Smooth scroll** | ✅ `html{scroll-behavior:smooth}` with `scroll-padding-top` |
| **Lazy loading** | ✅ All images use `loading="lazy"` |
| **Shadow system** | ✅ Two tiers: `--shadow` (subtle) and `--shadow-lg` (hover/cards) |
| **Border radius** | ✅ Consistent `--radius:12px` and `--radius-sm:8px` usage |
| **Button system** | ✅ `.btn`, `.btn-primary`, `.btn-outline`, `.btn-white` well-defined |

---

## P1 Fixes Applied

### 1. CTA button contrast — 3 pages
**Problem**: `tentang.html`, `layanan.html`, `kontak.html` used `btn-primary` (teal text on dark teal gradient CTA) — poor contrast/invisible.  
**Fix**: Changed to `btn-white` to match `index.html` and `produk.html`.  
**Files**: `tentang.html`, `layanan.html`, `kontak.html`

### 2. Focus-visible styles — missing
**Problem**: No `:focus-visible` rules → keyboard users get no focus indicator on any interactive element.  
**Fix**: Added focus-visible styles for `a`, `button`, `input`, `textarea`, `select`, `[tabindex]`, `.btn`, `.hamburger`.  
**File**: `style.css`

### 3. Text selection styling — missing
**Problem**: Default browser selection colors (often blue).  
**Fix**: Added `::selection{background:var(--accent);color:#fff}` for branded selection.  
**File**: `style.css`

### 4. Brand grid mobile collapse — produk.html
**Problem**: Brand partner grid uses inline `repeat(5,1fr)` which wouldn't collapse properly (original catch-all was too broad, collapsing 5-col to 1-col looks bad).  
**Fix**: Targeted overrides: `1fr 1fr` → `1fr`, `repeat(5` → `repeat(2,1fr)`.  
**File**: `style.css`

---

## P2 Issues (Noted, Not Fixed)

| # | Issue | Pages | Notes |
|---|-------|-------|-------|
| 1 | **Inline styles on hero** | index.html | Hero section uses ~15 inline `style=` attrs. Should be CSS classes for maintainability. |
| 2 | **Hero border-radius uses `20px`** | index.html, tentang.html | Hardcoded `20px` vs `--radius:12px`. Intentional but inconsistent. |
| 3 | **No reduced-motion media query** | style.css | Should add `@media(prefers-reduced-motion:reduce)` to disable animations for accessibility. |
| 4 | **CTA section uses `btn-primary` on dark bg in galeri.html** | galeri.html | No CTA section exists — gallery page jumps straight to footer. Could benefit from CTA. |
| 5 | **Inline grid on visi/misi section** | tentang.html | `grid-template-columns:1fr 1fr` inline — should be a CSS class. |
| 6 | **No `prefers-color-scheme` support** | style.css | No dark mode. P2 for future enhancement. |

---

## Files Modified

| File | Changes |
|------|---------|
| `style.css` | +focus-visible rules, +::selection, fixed mobile grid overrides |
| `tentang.html` | CTA button `btn-primary` → `btn-white` |
| `layanan.html` | CTA button `btn-primary` → `btn-white` |
| `kontak.html` | CTA button `btn-primary` → `btn-white` |

---

## Design System Health: 8/10

Strong foundation. CSS variable system, responsive breakpoints, card component patterns all solid. The main gap is accessibility (focus-visible was missing) and some inline style drift on the homepage hero.
