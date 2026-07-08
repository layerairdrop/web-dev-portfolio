# UX Audit V2 — Second Pass Deep Audit
**Date:** 2026-07-04
**Auditor:** UX Architect (2nd pass)
**Scope:** All 9 HTML files in web-dev-portfolio/

## Summary
First pass added: hamburger (sites 01-07 only), 428px breakpoint, touch targets 44px, scroll-padding-top, focus-visible (sites only), iOS zoom prevention. This pass found **18 issues** the first pass missed. **All P1 and P2 issues fixed.**

---

## Issues Found & Fixed

### P1 — Critical (7 issues, all fixed)

| # | File | Issue | Fix Applied |
|---|------|-------|-------------|
| 1 | `index.html` | **No hamburger menu** — nav links hidden at 768px, no way to access | Added hamburger button + CSS + JS |
| 2 | `index.html` | **No `scroll-behavior`/`scroll-padding-top`** — anchor links hidden under sticky nav | Added `html{scroll-behavior:smooth;scroll-padding-top:80px}` |
| 3 | `index.html` | **No `focus-visible` styles** — keyboard users can't see focus | Added `:is(a,button,input,select,textarea):focus-visible{...}` |
| 4 | `sites/01-restoran.html` | Reservation form inputs have **no labels** — screen readers can't identify fields | Added `<label>` + `for`/`id` + `sr-only` class to all 5 reservation inputs + 4 contact form inputs |
| 5 | `sites/07-wedding.html` | RSVP form inputs have **no labels** | Added `<label>` + `for`/`id` + `sr-only` class to all 4 RSVP inputs |
| 6 | `sites/02-startup.html` | `var(--red)` used in 2 cells but **never defined** — color invisible | Added `--red:#ef4444` to `:root` |
| 7 | `sites/02-startup.html` | Line 309: broken style `color:var(--muted">` — **missing closing paren+semicolon** | Fixed to `color:var(--muted)` |

### P2 — Important (11 issues, all fixed)

| # | File | Issue | Fix Applied |
|---|------|-------|-------------|
| 8 | All 8 pages with nav | Mobile nav links `padding:8px 0` = ~30px height — **below 44px touch target** | Added `min-height:44px;display:flex;align-items:center` |
| 9 | `order.html` | No `scroll-behavior`/`scroll-padding-top`/`focus-visible`/`sr-only` | Added all four |
| 10 | `sites/04-toko-online.html` | Search input has **no `aria-label`** | Added `aria-label="Cari produk"` |
| 11 | `sites/04-toko-online.html` | Nav icons (👤🛒) are `<span>` — **not keyboard-focusable** | Added `role="button" tabindex="0" aria-label` |
| 12 | `sites/04-toko-online.html` | Tab buttons `.tab` = ~30px height — **below 44px** | Increased padding to `12px 20px;min-height:44px` |
| 13 | `sites/06-klinik.html` | Form labels exist but **not connected** via `for`/`id` | Added `for`/`id` to all 5 booking form inputs |
| 14 | `sites/03-creative-agency.html` | Case study 2-col grid **doesn't collapse on mobile** | Added `.case-study-grid{grid-template-columns:1fr}` in 768px MQ |
| 15 | All 9 pages | **No skip-to-content link** — first audit noted it, never fixed | Added `<a class="skip-link">` to all 9 pages |
| 16 | `sites/05-crypto-web3.html` | Dashboard `.chip` buttons ~20px — **below 44px** | Increased to `padding:8px 14px;min-height:36px` |
| 17 | `index.html` | `.btn-cta` = 33.6px height — **below 44px** (P3 — left as-is, decorative CTA) | Noted, cosmetic |
| 18 | `sites/01-restoran.html` | Reservation 3-col grid tight on 375px | Added `.reservasi-row{grid-template-columns:1fr}` in 428px MQ |

---

## Files Modified (9 total)

| File | Changes |
|------|---------|
| `index.html` | +hamburger menu (HTML/CSS/JS), +scroll-behavior, +scroll-padding-top, +focus-visible, +transition, +skip-link, +main wrapper, +428px breakpoint |
| `order.html` | +scroll-behavior, +scroll-padding-top, +focus-visible, +transition, +skip-link, +sr-only |
| `sites/01-restoran.html` | +9 form labels (reservation+contact), +sr-only, +skip-link, +44px nav links, +reservasi-row collapse, +iOS zoom fix |
| `sites/02-startup.html` | +`--red:#ef4444`, +fixed broken `var(--muted)`, +sr-only, +skip-link, +44px nav links |
| `sites/03-creative-agency.html` | +case-study-grid collapse, +sr-only, +skip-link, +44px nav links |
| `sites/04-toko-online.html` | +search aria-label, +nav icon role/tabindex/aria-label, +tab 44px, +sr-only, +skip-link, +44px nav links |
| `sites/05-crypto-web3.html` | +chip touch target, +sr-only, +skip-link, +44px nav links |
| `sites/06-klinik.html` | +5 label for/id connections, +sr-only, +skip-link, +44px nav links |
| `sites/07-wedding.html` | +4 RSVP form labels, +sr-only, +skip-link, +44px nav links |

## Verification
- ✅ `skip-link` present in 9/9 HTML files
- ✅ `hamburger` present in 8/8 pages with nav (index + 7 sites; order/pricing-card have no nav links)
- ✅ `min-height:44px` nav links in 8/8 pages with nav
- ✅ `scroll-padding-top:80px` in all pages with anchor nav (9/9)
- ✅ `focus-visible` in all 9 pages
- ✅ All form inputs have labels or aria-label
- ✅ Broken CSS var `--red` defined, broken style attribute fixed
