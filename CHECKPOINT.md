# LYID Web Dev Portfolio — Checkpoint
# Updated: 2026-07-09
# Purpose: Track portfolio site status + audit state

## Current State
- **Production URL**: https://www.ralies.biz.id
- **Vercel Project**: agent-hub-avax/lyid-web-dev-portfolio
- **Total Sites**: 13 demo sites
- **Audit Status**: 16/16 clean (0 issues) — verified 2026-07-08

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
