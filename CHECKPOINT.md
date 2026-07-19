# LYID Web Dev Portfolio — Checkpoint
# Updated: 2026-07-19
# Purpose: Track portfolio site status + audit state

## Current State
- **Production URL**: https://www.ralies.biz.id
- **Vercel Project**: agent-hub-avax/lyid-web-dev-portfolio
- **GitHub Repo**: layerairdrop/web-dev-portfolio (PUBLIC, branch master)
- **Total Sites**: 13 demo sites
- **Audit Status**: 16/16 clean (2026-07-08) + Hallmark anti-slop gradient audit (2026-07-19)

## Recent Changes (2026-07-19)
- Reduced AI-slop gradient usage 6→3 spots per Hallmark audit (commit 4a5d625)
  - Removed gradient from: .btn-cta, .btn-primary, .btn-card.filled, .process-num
  - Kept gradient only for: .logo-mark, .hero h1 .grad, #progressBar
- Full Hallmark anti-slop batch fix across 42 files (commits e218bfa, b29a818, d45572e, 4390362)
  - Inter→Plus Jakarta Sans + DM Serif Display (font pairing)
  - Gradient headline (.grad)→solid text
  - Purple hero blob→blue-only radial gradient
  - Purple CTA blob→blue-only
  - Section-label eyebrow removal (Portfolio, Pricing, Process, etc.)
  - Generic emoji badges→text symbols (✦, →, ◆, —)
  - Purple shadow-glow→tight dark shadow
  - Hero text-align:left bias (was center)
  - Fade-in: hero-only (was every section)
  - transition:all→specific properties
  - 5 inline styles→CSS classes
  - Nav N1a→N5 floating pill (logo + pill nav + CTA, desktop + mobile)
  - Section titles/subtitles left-align (was center everywhere)
  - Subfolder sites batch: properti-premium, edu-academy, grand-hotel, hukum-pratama, yayasan-harapan
- Repo visibility changed: private → public (Hobby plan cannot link private org repo)
- Vercel auth token rotated to new account (rmndkyl), then reverted to agenthubavax
- Deployment via CLI unreliable on Windows/MSYS — prefer Vercel Dashboard manual Redeploy
- Verified: layerairdrop/web-dev-portfolio is public and Vercel GitHub App linked

## Site Inventory
| # | Slug | Industry | Pages | Design Tier | Status |
|---|------|----------|-------|-------------|--------|
| 01 | 01-restoran.html | F&B | 1 | Standard | ✅ Live |
| 02 | 02-startup.html | SaaS | 1 | Standard | ✅ Live |
| 03 | 03-creative-agency.html | Creative | 1 | Standard | ✅ Live |
| 04 | 04-toko-online.html | E-Commerce | 1 | Standard | ✅ Live |
| 05 | 05-crypto-web3.html | Crypto/Web3 | 1 | Standard | ✅ Live |
| 06 | 06-klinik.html | Healthcare | 1 | Standard | ✅ Live |
| 07 | 07-wedding.html | Event | 1 | Standard | ✅ Live |
| 08 | 08-company-profile-demo.html | Medical | 1 | Standard | ✅ Live |
| 09 | maju-bersama/ | Medical/Alkes | 6 (consolidated) | Standard | ✅ Live |
| 10 | properti-premium/ | Property | 1 (consolidated) | Premium | ✅ Live |
| 11 | edu-academy/ | Education | 1 (consolidated) | Standard | ✅ Live |
| 12 | grand-hotel/ | Hospitality | 1 (consolidated) | Standard | ✅ Live |
| 13 | hukum-pratama/ | Legal | 1 (consolidated) | Standard | ✅ Live |
| 14 | yayasan-harapan/ | NGO | 1 (consolidated) | Standard | ✅ Live |

Note: Sites 09-14 were multi-page, consolidated to single index.html on 2026-07-08.

## Design Standards
- **Brand colors**: BG #09090b, Blue #3b82f6, Purple #8b5cf6
- **Font**: Plus Jakarta Sans (body) + DM Serif Display (headings)
- **GA4**: G-C6BH106VBQ (all sites)
- **WhatsApp**: 6287897299985 (all sites)
- **LYID credit**: "Dibuat oleh LYID Web Development" (all sites)

## Audit Scripts
| Script | Purpose |
|--------|---------|
| `audit_sites.py` | Scan HTML + CSS for P1/P2/P3 issues |
| `fix_audit.py` | Auto-inject OG, GA4, WhatsApp, CSS patterns |
| `upgrade_sites.py` | Batch upgrade to MotionSites template |

## Recent Changes (2026-07-08)
- Upgraded 6 sites to MotionSites premium cinematic design
- Consolidated multi-page sites to single index.html
- Added OG tags to all 16 sites
- Fixed aria-expanded on 2 sites (08, maju-bersama)
- Deployed to production: vercel --prod --yes
