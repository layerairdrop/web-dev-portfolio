# FindRealEstate.com — Design Research

> Deep-dive analysis of https://findrealestate.com/ design patterns.
> Purpose: Extract premium design patterns untuk diterapkan ke LYID portfolio.

## 1. Design Aesthetic
- **Mood:** Clean, modern, premium tapi approachable. Editorial feel.
- **Layout:** Full-width sections, generous whitespace
- **Brand:** Premium real estate — sophisticated minimalism
- **CSS:** CSS Modules dengan BEM-like naming

## 2. Typography
- **Font:** "Instrument Sans" (Google Fonts, variable weight)
- **H1:** ~92px, weight 700, letter-spacing -1.84px (tight negative)
- **Body:** ~21px, weight 400, line-height 1.3
- **H3:** White on dark backgrounds
- **Key:** Extreme H1 size + tight spacing = dramatic impact

## 3. Color Palette
```css
--black: rgb(21, 23, 23);     /* #151717 — primary dark */
--white: rgb(255, 255, 255);  /* #FFFFFF */
--gray: rgb(241, 241, 241);   /* #F1F1F1 — light bg */
```
Strategy: Almost exclusively black + white + near-black + light gray. Extremely restrained.

## 4. Hero Section
- Full viewport height with layered images
- Background: 3840×2612px (2x retina), lazy loaded
- Foreground house: PNG with transparency, eager loaded
- GSAP parallax: translate3d + scale on scroll
- CTA: "Find Properties" button with arrow icon
- Copy: H1 = "Find What Moves You"

## 5. Navigation
- Sticky header, transparent → solid on scroll
- Auto-hide on scroll down (`header_-hidden__CVUoR`)
- Desktop: horizontal nav with dropdown arrows
- Mobile: burger menu
- Sign In prominent on right

## 6. Button Styles
- Sharp corners (border-radius: 0)
- Dark bg (#151717) + white text
- Arrow SVG icon inside
- Duplicate text spans for stagger animation
- Same style across all 7 CTAs

## 7. Sections (Top → Bottom)
1. Hero — transparent bg, image parallax
2. Why FIND — white bg, video + text
3. Steps (01-03) — process walkthrough
4. For Agents — transparent bg, image/video
5. Testimonials — light gray #F1F1F1, carousel
6. Services — dark #151717, accordion (Buy/Sell/Rent)
7. Support Beyond — dark bg, cards
8. Blog/Resources — cards
9. Bottom CTA — dark bg
10. Footer — dark bg, newsletter + links

## 8. Animations (GSAP)
- Scroll-triggered reveals: opacity 0→1, translateY(-40%)→0, scale(0.98)→1
- Hero parallax: translate3d on background + foreground images
- Text stagger animation via duplicate spans + data-text attributes
- All powered by GSAP ScrollTrigger

## 9. CTA Pattern
7 CTAs throughout page, ALL same style:
1. "Find Properties" — Hero
2. "Start Your Search" — Why FIND
3. "Join The Movement" — For Agents
4. "Get Started with FIND" — Services
5. "Discover Our Services" — Support
6. "Visit Our Blog" — Blog
7. "Let's Get Started" — Bottom

## 10. CSS Values to Copy
```css
/* Core palette */
--black: #151717;
--white: #FFFFFF;
--gray: #F1F1F1;

/* Typography */
--font: "Instrument Sans", sans-serif;
--h1-size: clamp(3rem, 6vw, 6rem);
--h1-weight: 700;
--h1-spacing: -0.02em;
--body-size: 1.3rem;
--body-lh: 1.3;

/* Buttons */
border-radius: 0;
background: var(--black);
color: var(--white);
border: 1px solid transparent;
```

## Key Takeaways
1. **Typography scale** — extreme H1 (92px) with tight spacing = instant premium
2. **Color restraint** — almost monochrome (black/white/gray) = sophisticated
3. **GSAP animations** — parallax, scroll reveals, text stagger = cinematic
4. **Sharp buttons** — border-radius: 0 = modern editorial feel
5. **Dark/light alternation** — sections alternate between white and #151717
6. **Arrow CTAs** — every button has arrow icon, consistent pattern
7. **Transparent header** — sticky + transparent → solid on scroll
8. **Accordion services** — numbered items (01/02/03) for engagement
