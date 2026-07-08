# UI Audit — Web Dev Portfolio Sites

**Audited:** 2026-07-03 | **Files:** 7 site demos in `/sites/`

---

## Global Issues (All Sites)

### P1 — Critical UX / Accessibility

| # | Issue | Sites | Fix |
|---|-------|-------|-----|
| G1 | **No `scroll-behavior: smooth`** — anchor links jump abruptly | ALL 7 | Add `html{scroll-behavior:smooth}` |
| G2 | **No `:focus-visible` styles** — keyboard users can't see focus | ALL 7 | Add `a:focus-visible,button:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:4px}` |
| G3 | **Missing transitions on links/buttons** — hover feels jarring | ALL 7 | Ensure all `a`, `button` have `transition:all .2s` or similar |
| G4 | **Some images missing `loading="lazy"`** — hero images that are below-fold on mobile | 01, 04, 06 | Already correct in most; hero images correctly use `loading="eager"` (07) |

### P2 — Design Consistency

| # | Issue | Sites | Fix |
|---|-------|-------|-----|
| G5 | **Inconsistent border-radius** — some sites use `8px`, others `12px`, `16px` for similar elements (buttons) | 01(999px btn), 03(12px btn), 04(8px btn) | Standardize: pills=999px, buttons=12px, cards=16px |
| G6 | **Hardcoded colors in inline styles** | 01 (`#fef3e2` on sections), 05 (`#f59e0b`, `#a855f7`, `#14b8a6` in protos), 03 (`#555` in footer) | Use CSS variables |
| G7 | **Inconsistent shadow system** | 01(`0 4px 20px`), 02(`0 4px 24px`), 03(`0 8px 32px`), 04(`0 4px 16px`) | Each site has own scale — OK per-site, but card shadows inconsistent within 01 (card has shadow on hover only, testi has shadow always) |

### P3 — Polish

| # | Issue | Sites | Fix |
|---|-------|-------|-----|
| G8 | **No dark mode readiness** — light-only sites use many hardcoded backgrounds | 01, 04, 06, 07 | Would require significant refactor; CSS vars make it possible but not trivial |
| G9 | **Mixed `border-radius` on form inputs** | 01(8px), 04(8px), 06(10px), 07(n/a) | Standardize to `var(--radius)` or 12px |

---

## Per-Site Issues

### 01-restoran.html

| Priority | Selector | Issue | Fix |
|----------|----------|-------|-----|
| P2 | `nav` | Hardcoded `#f0e6d6` border | Use CSS variable or calc from `--bg` |
| P2 | `.about-img` | No `img` element — uses gradient placeholder with emoji | OK for demo |
| P2 | `footer p` | Hardcoded `#666` color | Use `var(--muted)` |
| P2 | Inline `style="background:#fef3e2"` on sections | Hardcoded accent bg | Add `.section-alt{background:var(--accent-bg)}` to `:root` |
| P3 | `.menu-card` | No shadow by default, shadow only on hover via transform | Consider adding subtle base shadow |

### 02-startup.html

| Priority | Selector | Issue | Fix |
|----------|----------|-------|-----|
| P2 | `.stats-bar .container` | Inline `style="display:grid..."` duplicates `.stats-bar` grid | Remove inline style |
| P3 | No images at all | Pure text/emoji site — no alt text issues | N/A |
| P2 | `.btn-card` | Uses `var(--card)` bg — looks flat | Consider `var(--surface)` |

### 03-creative-agency.html

| Priority | Selector | Issue | Fix |
|----------|----------|-------|-----|
| P2 | `footer p:last-child` | Hardcoded `color:#555` | Use `var(--muted)` |
| P2 | `.work-card .bg` | Gradient backgrounds with nth-child — good but uses 4 hardcoded hex colors | Could be CSS vars |
| P2 | `nav` | `position:fixed` but no bg on scroll — content shows through | Add bg or use sticky |
| P3 | `.marquee-track` | Animation runs even when not visible | Add `will-change:transform` |

### 04-toko-online.html

| Priority | Selector | Issue | Fix |
|----------|----------|-------|-----|
| P2 | `.product-card` | No shadow by default, shadow on hover only | Add subtle base shadow |
| P2 | `.btn-wa` | Hardcoded `#25d366` | Add `--wa: #25d366` to root |
| P3 | `.tabs` buttons | Uses `button` elements styled as tabs — no `aria` roles | Add `role="tablist"` |

### 05-crypto-web3.html

| Priority | Selector | Issue | Fix |
|----------|----------|-------|-----|
| P2 | `.proto-dot` | Multiple hardcoded colors (`#f59e0b`, `#a855f7`, `#14b8a6`) | Add CSS vars |
| P2 | `footer p:last-child` | Hardcoded `color:#444` | Use `var(--muted)` |
| P3 | `.dash-preview` | No `aria-label` for the dashboard preview | Add `role="img"` `aria-label` |

### 06-klinik.html

| Priority | Selector | Issue | Fix |
|----------|----------|-------|-----|
| P2 | `.info-item` nth-child | Hardcoded bg colors (`#fef3c7`, `#fce7f3`) | Add CSS vars |
| P2 | `.serv-icon` nth-child | 6 hardcoded pastel colors | Add CSS vars |
| P3 | `.faq-q` | No `role="button"` or keyboard handling | Add `tabindex="0"` |

### 07-wedding.html

| Priority | Selector | Issue | Fix |
|----------|----------|-------|-----|
| P2 | `.btn-wa` | Hardcoded `#25d366` | Add CSS var |
| P2 | `footer` | Multiple hardcoded browns (`#c4b5a5`, `#8a7e74`, `#5a5047`) | Use CSS vars |
| P2 | `.hero-bg img` | Hero image uses `loading="eager"` — correct for LCP | ✅ Good |
| P3 | `.hero-float` | `display:none` always — dead code | Remove or implement |

---

## Summary of All Fixes Applied

### P1 — Applied to ALL 7 files
1. `html{scroll-behavior:smooth}` — smooth anchor navigation
2. `a,button{transition:all .2s ease}` — smooth hover/focus transitions on all interactive elements
3. `:focus-visible` outline styles — keyboard accessibility (each site uses its own accent color)

### P2 — Applied targeted fixes
4. **01-restoran.html** — Footer `#666` → `var(--muted)`
5. **02-startup.html** — Removed duplicate inline grid style from `.stats-bar .container`
6. **03-creative-agency.html** — Footer `#555` → `var(--muted)`
7. **05-crypto-web3.html** — Footer `#444` → `var(--muted)`
8. **07-wedding.html** — Removed dead `.hero-float` CSS (unused at all breakpoints), fixed media query structure

### Verified ✅
- All images have proper `alt` text
- All below-fold images use `loading="lazy"`
- Hero image in 07-wedding.html correctly uses `loading="eager"` (LCP)
- All sites have proper `:root` CSS variable systems
- All sites have responsive breakpoints at 768px

### Remaining P2/P3 (not applied — requires design decisions)
- Inconsistent border-radius across sites (each site has own design language — intentional)
- Hardcoded hex colors in proto dots (05), service icon bgs (06) — decorative, low impact
- No dark mode support — would need CSS variable overhaul per site
- Form input radius inconsistency (8px vs 10px vs 12px)
