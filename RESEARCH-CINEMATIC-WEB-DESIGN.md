# Cinematic & Premium Web Design Animation Techniques

> Research for upgrading LYID Web Dev portfolio from basic → cinematic/premium quality.
> Stack: Vanilla HTML/CSS/JS, Google Fonts, no build tools, static HTML.

---

## Table of Contents

1. [Image Animations](#1-image-animations)
2. [Section Transitions](#2-section-transitions)
3. [CSS Timing & Easing](#3-css-timing--easing)
4. [Cinematic Premium Feel](#4-cinematic-premium-feel)
5. [Modern CSS APIs](#5-modern-css-apis)
6. [Performance Bible](#6-performance-bible)
7. [Libraries Reference](#7-libraries-reference)
8. [Implementation Priority](#8-implementation-priority-for-lyid-portfolio)

---

## 1. Image Animations

### 1.1 Pan — Horizontal Movement on Scroll

**Technique:** Use `scroll-timeline` or Intersection Observer to drive `translateX` based on scroll position.

```css
/* Pure CSS — scroll-driven (Chrome 115+, Safari 18.2+) */
.pan-image {
  animation: pan-across linear both;
  animation-timeline: view();
  animation-range: entry 0% exit 100%;
}

@keyframes pan-across {
  from { transform: translateX(-10%); }
  to   { transform: translateX(10%); }
}
```

```js
// Vanilla JS fallback — Intersection Observer + scroll listener
function initPanImages() {
  const images = document.querySelectorAll('.pan-on-scroll');
  
  window.addEventListener('scroll', () => {
    images.forEach(img => {
      const rect = img.getBoundingClientRect();
      const progress = (window.innerHeight - rect.top) / (window.innerHeight + rect.height);
      const clamped = Math.max(0, Math.min(1, progress));
      const offset = -10 + (clamped * 20); // -10% to +10%
      img.style.transform = `translateX(${offset}%)`;
    });
  }, { passive: true });
}
```

**Browser compat:** CSS version: Chrome 115+, Safari 18.2+. JS fallback: all browsers.
**Performance:** Use `will-change: transform` on the element. Always animate `transform`, never `left`. Use `{ passive: true }` on scroll listener. Throttle with `requestAnimationFrame`.
**When to use:** Portfolio project cards, gallery sections, testimonials.

---

### 1.2 Zoom — Scale on Scroll or Hover

**Technique:** Scale image from 1.0 → 1.15 as it enters viewport. On hover, scale to 1.05 with smooth transition.

```css
/* Scroll-driven zoom */
.zoom-scroll {
  transform: scale(1);
  will-change: transform;
  animation: zoom-in linear both;
  animation-timeline: view();
  animation-range: entry 0% cover 50%;
}

@keyframes zoom-in {
  from { transform: scale(1); }
  to   { transform: scale(1.15); }
}

/* Hover zoom with overflow hidden on parent */
.zoom-hover-wrapper {
  overflow: hidden;
  border-radius: 12px;
}

.zoom-hover-wrapper img {
  transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.zoom-hover-wrapper:hover img {
  transform: scale(1.08);
}
```

```js
// JS scroll-driven zoom
function initZoomScroll() {
  const elements = document.querySelectorAll('.zoom-scroll');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
      }
    });
  }, { threshold: 0.2 });

  elements.forEach(el => observer.observe(el));

  window.addEventListener('scroll', () => {
    elements.forEach(el => {
      if (!el.classList.contains('in-view')) return;
      const rect = el.getBoundingClientRect();
      const progress = 1 - (rect.top / window.innerHeight);
      const scale = 1 + Math.min(0.15, Math.max(0, progress * 0.15));
      el.style.transform = `scale(${scale})`;
    });
  }, { passive: true });
}
```

**Browser compat:** All browsers (JS). CSS scroll-timeline: Chrome 115+, Safari 18.2+.
**Performance:** `transform: scale()` is GPU-composited. Add `will-change: transform`. Always `overflow: hidden` on parent for hover zoom.
**When to use:** Hero images, project showcase thumbnails, team photos.

---

### 1.3 Tilt — 3D Perspective on Mouse Move

**Technique:** Track mouse position relative to element center, apply `rotateX`/`rotateY` via JS.

```css
.tilt-card {
  perspective: 1000px;
  transform-style: preserve-3d;
  transition: transform 0.3s ease-out;
  will-change: transform;
}
```

```js
function initTiltCards() {
  document.querySelectorAll('.tilt-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = ((y - centerY) / centerY) * -10; // max ±10deg
      const rotateY = ((x - centerX) / centerX) * 10;

      card.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'rotateX(0) rotateY(0) scale3d(1, 1, 1)';
    });
  });
}
```

**Browser compat:** All modern browsers. `perspective` supported everywhere.
**Performance:** `transform` with 3D values triggers GPU compositing. Limit to max ±12deg for subtlety. Use `requestAnimationFrame` for smooth updates. Don't apply to more than 3-4 elements simultaneously.
**When to use:** Project cards, skill badges, about section cards, CTA blocks.

---

### 1.4 Parallax — Multi-Layer Depth on Scroll

**Technique:** Multiple layers move at different speeds. Closer = faster, farther = slower.

```css
.parallax-container {
  position: relative;
  overflow: hidden;
  height: 100vh;
}

.parallax-layer {
  position: absolute;
  inset: 0;
  will-change: transform;
}

.parallax-bg    { transform: translateZ(-2px) scale(3); }  /* slowest */
.parallax-mid   { transform: translateZ(-1px) scale(2); }  /* medium */
.parallax-fg    { transform: translateZ(0); }               /* normal */
```

```css
/* Pure CSS parallax (no JS) — uses 3D perspective trick */
.parallax-pure-css {
  perspective: 1px;
  height: 100vh;
  overflow-x: hidden;
  overflow-y: auto;
  perspective-origin: center center;
}

.parallax-pure-css .bg-layer {
  position: absolute;
  inset: 0;
  transform: translateZ(-1px) scale(2); /* Moves slower than scroll */
}

.parallax-pure-css .content-layer {
  position: relative;
  transform: translateZ(0); /* Normal scroll speed */
}
```

```js
// JS Parallax — most flexible
function initParallax() {
  const layers = document.querySelectorAll('[data-parallax-speed]');

  window.addEventListener('scroll', () => {
    requestAnimationFrame(() => {
      layers.forEach(layer => {
        const speed = parseFloat(layer.dataset.parallaxSpeed) || 0.5;
        const rect = layer.parentElement.getBoundingClientRect();
        const offset = rect.top * speed;
        layer.style.transform = `translate3d(0, ${offset}px, 0)`;
      });
    });
  }, { passive: true });
}
```

**Browser compat:** Pure CSS: Chrome/Safari/Edge (3D transforms). Firefox has quirks. JS: all.
**Performance:** Always use `transform: translate3d()` to force GPU layer. Never use `top`/`margin-top`. Limit to 2-3 layers. Use `will-change: transform` on each layer. On mobile, consider reducing or disabling parallax.
**When to use:** Hero sections, full-width banner sections, "about" splash area.

---

### 1.5 Ken Burns Effect — Slow Zoom + Pan on Images

**Technique:** CSS keyframe animation combining `scale` and `translate` over long duration (15-25s), looping.

```css
.ken-burns {
  overflow: hidden;
  position: relative;
}

.ken-burns img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  animation: ken-burns-1 20s ease-in-out infinite alternate;
}

@keyframes ken-burns-1 {
  0%   { transform: scale(1)    translate(0, 0); }
  50%  { transform: scale(1.15) translate(-3%, -2%); }
  100% { transform: scale(1.1)  translate(2%, -1%); }
}

/* Alternate direction for hero slides */
@keyframes ken-burns-2 {
  0%   { transform: scale(1.1)  translate(3%, 1%); }
  50%  { transform: scale(1)    translate(-2%, 2%); }
  100% { transform: scale(1.15) translate(1%, -3%); }
}

/* Crossfade between multiple Ken Burns images */
.ken-burns-slide {
  position: absolute;
  inset: 0;
  opacity: 0;
  animation: ken-fade 12s infinite;
}

.ken-burns-slide:nth-child(1) { animation-delay: 0s; }
.ken-burns-slide:nth-child(2) { animation-delay: 4s; }
.ken-burns-slide:nth-child(3) { animation-delay: 8s; }

@keyframes ken-fade {
  0%, 25%  { opacity: 0; }
  33%, 66% { opacity: 1; }
  75%, 100%{ opacity: 0; }
}
```

**Browser compat:** All browsers. Pure CSS.
**Performance:** GPU-composited (`transform` only). Very lightweight. Images should be loaded but can be lazy if only 1-2 visible.
**When to use:** Hero sections with multiple background images, portfolio project hero, about page splash.

---

## 2. Section Transitions

### 2.1 Smooth Masks — clip-path Animations Between Sections

**Technique:** Use `clip-path` polygon/circle transitions to reveal sections creatively.

```css
/* Circle reveal on scroll */
.reveal-circle {
  clip-path: circle(0% at 50% 50%);
  transition: clip-path 1s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.reveal-circle.in-view {
  clip-path: circle(75% at 50% 50%);
}

/* Diagonal wipe */
.reveal-diagonal {
  clip-path: polygon(0 0, 0 0, 0 100%, 0 100%);
  transition: clip-path 0.8s cubic-bezier(0.77, 0, 0.175, 1);
}

.reveal-diagonal.in-view {
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
}

/* Diamond reveal */
.reveal-diamond {
  clip-path: polygon(50% 50%, 50% 50%, 50% 50%, 50% 50%);
  transition: clip-path 1.2s cubic-bezier(0.65, 0, 0.35, 1);
}

.reveal-diamond.in-view {
  clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
}

/* Scroll-driven clip-path (no JS needed) */
.clip-reveal {
  clip-path: inset(0 100% 0 0);
  animation: clip-slide linear both;
  animation-timeline: view();
  animation-range: entry 0% cover 30%;
}

@keyframes clip-slide {
  to { clip-path: inset(0 0 0 0); }
}
```

**Browser compat:** `clip-path` — all modern browsers. `animation-timeline: view()` — Chrome 115+, Safari 18.2+.
**Performance:** `clip-path` is composited when using `polygon`, `circle`, `inset`. Animating `clip-path` triggers repaint but is generally smooth. Avoid animating `clip-path` on very large elements on low-end mobile.
**When to use:** Hero section reveals, image reveals in portfolio, section separators.

---

### 2.2 Fade-In on Scroll — Intersection Observer Patterns

**Technique:** Detect when element enters viewport, add `.in-view` class to trigger CSS transitions.

```css
/* Base hidden state */
.fade-up {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s ease-out, transform 0.8s ease-out;
  will-change: opacity, transform;
}

.fade-up.in-view {
  opacity: 1;
  transform: translateY(0);
}

/* Stagger support */
.fade-up-delay-1 { transition-delay: 0.1s; }
.fade-up-delay-2 { transition-delay: 0.2s; }
.fade-up-delay-3 { transition-delay: 0.3s; }
.fade-up-delay-4 { transition-delay: 0.4s; }
```

```js
// Intersection Observer — the core pattern
function initScrollAnimations() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        observer.unobserve(entry.target); // animate once
      }
    });
  }, {
    threshold: 0.15,       // trigger when 15% visible
    rootMargin: '0px 0px -50px 0px' // trigger slightly before full view
  });

  document.querySelectorAll('.fade-up, .fade-in, .reveal-left, .reveal-right')
    .forEach(el => observer.observe(el));
}

document.addEventListener('DOMContentLoaded', initScrollAnimations);
```

```css
/* Variants */
.fade-in {
  opacity: 0;
  transition: opacity 0.6s ease-out;
}
.fade-in.in-view { opacity: 1; }

.reveal-left {
  opacity: 0;
  transform: translateX(-60px);
  transition: opacity 0.7s ease-out, transform 0.7s ease-out;
}
.reveal-left.in-view {
  opacity: 1;
  transform: translateX(0);
}

.reveal-right {
  opacity: 0;
  transform: translateX(60px);
  transition: opacity 0.7s ease-out, transform 0.7s ease-out;
}
.reveal-right.in-view {
  opacity: 1;
  transform: translateX(0);
}

.scale-in {
  opacity: 0;
  transform: scale(0.9);
  transition: opacity 0.6s ease-out, transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.scale-in.in-view {
  opacity: 1;
  transform: scale(1);
}
```

**Browser compat:** Intersection Observer — Chrome 51+, Firefox 55+, Safari 12.1+. Excellent support.
**Performance:** Intersection Observer is async and non-blocking. Much better than scroll event listeners. Unobserve after trigger to stop observing. Use `will-change` sparingly (only during transition).
**When to use:** Every section below the fold. This is the bread-and-butter of premium feel. Use for text blocks, images, cards, buttons — everything.

---

### 2.3 Crossfade Between Hero Sections

**Technique:** Multiple hero images/sections with absolute positioning, cycling opacity via CSS animation or JS timer.

```css
.hero-crossfade {
  position: relative;
  height: 100vh;
  overflow: hidden;
}

.hero-slide {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity 1.5s ease-in-out;
}

.hero-slide.active {
  opacity: 1;
}
```

```js
function initHeroCrossfade() {
  const slides = document.querySelectorAll('.hero-slide');
  let current = 0;

  // Set first slide active
  slides[0].classList.add('active');

  setInterval(() => {
    slides[current].classList.remove('active');
    current = (current + 1) % slides.length;
    slides[current].classList.add('active');
  }, 5000); // 5 seconds per slide
}
```

**Browser compat:** All browsers.
**Performance:** `opacity` is GPU-composited. No performance concerns.
**When to use:** Homepage hero with multiple project showcases, landing page intro.

---

### 2.4 Reveal Animations — Text Slide-Up, Image Uncover

**Technique:** Clip or mask text lines to reveal them with upward motion. Split text into words/lines for granular control.

```css
/* Text reveal — single line */
.reveal-text {
  overflow: hidden;
}

.reveal-text-inner {
  display: inline-block;
  transform: translateY(100%);
  transition: transform 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.reveal-text.in-view .reveal-text-inner {
  transform: translateY(0);
}

/* Multi-line reveal — stagger per line */
.reveal-lines .line {
  overflow: hidden;
}

.reveal-lines .line span {
  display: inline-block;
  transform: translateY(110%);
  transition: transform 0.7s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.reveal-lines.in-view .line span {
  transform: translateY(0);
}

.reveal-lines.in-view .line:nth-child(2) span { transition-delay: 0.1s; }
.reveal-lines.in-view .line:nth-child(3) span { transition-delay: 0.2s; }
.reveal-lines.in-view .line:nth-child(4) span { transition-delay: 0.3s; }

/* Image uncover — slide from left with mask */
.image-uncover {
  overflow: hidden;
}

.image-uncover img {
  width: 120%;
  transform: translateX(-20%);
  transition: transform 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.image-uncover.in-view img {
  transform: translateX(0);
}
```

```js
// Split text into lines for multi-line reveal
function splitTextIntoLines(el) {
  const text = el.textContent.trim();
  el.innerHTML = text.split(' ').map(word =>
    `<span style="display:inline-block">${word} </span>`
  ).join('');

  // Wrap each line (approximate by counting words per line)
  const spans = el.querySelectorAll('span');
  const containerWidth = el.offsetWidth;
  let currentLine = [];
  const lines = [[]];

  spans.forEach(span => {
    currentLine.push(span);
    el.innerHTML = lines.map(line =>
      `<div class="line">${line.map(s => s.outerHTML).join('')}</div>`
    ).join('') + currentLine.map(s => s.outerHTML).join('');

    if (el.querySelector('.line:last-child').offsetWidth >= containerWidth * 0.9) {
      lines.push([]);
      currentLine = [];
    }
  });
}
```

**Browser compat:** All browsers. `display: inline-block` + `transform: translateY` works everywhere.
**Performance:** `transform` is composited. `overflow: hidden` adds a new stacking context — fine for individual elements, avoid on containers with many children.
**When to use:** Hero headlines, section headings, any important text that should "arrive" with impact.

---

## 3. CSS Timing & Easing

### 3.1 Realistic Movement Curves — cubic-bezier for Natural Feel

```css
/* Material Design / Natural curves */
.ease-out-expo   { transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1); }
.ease-out-quart  { transition-timing-function: cubic-bezier(0.25, 1, 0.5, 1); }
.ease-out-cubic  { transition-timing-function: cubic-bezier(0.33, 1, 0.68, 1); }
.ease-in-out-expo { transition-timing-function: cubic-bezier(0.87, 0, 0.13, 1); }
.ease-spring     { transition-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1); } /* overshoot */
.ease-bounce     { transition-timing-function: cubic-bezier(0.68, -0.55, 0.265, 1.55); }
.ease-snap       { transition-timing-function: cubic-bezier(0.85, 0, 0.15, 1); }

/* Apple-style smooth deceleration */
.ease-apple      { transition-timing-function: cubic-bezier(0.25, 0.1, 0.25, 1); }

/* Premium page transitions */
.page-enter {
  animation: page-slide-in 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes page-slide-in {
  from { opacity: 0; transform: translateY(30px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

**When to use:**
- `ease-out-expo`: Most transitions (elements appearing, menus opening)
- `ease-spring`: Buttons, playful interactions, cards flipping
- `ease-out-cubic`: Default for scroll-triggered animations
- `ease-snap`: Snapping into position, tab switches
- `ease-in-out-expo`: Full-page transitions, smooth scroll

---

### 3.2 Spring Physics in CSS

```css
/* CSS doesn't have native spring physics, but we can simulate with cubic-bezier */

/* Subtle overshoot — like a gentle spring */
.spring-subtle {
  transition-timing-function: cubic-bezier(0.34, 1.3, 0.64, 1);
}

/* Medium bounce — card flip, modal open */
.spring-medium {
  transition-timing-function: cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

/* Big bounce — playful elements, emoji reactions */
.spring-big {
  transition-timing-function: cubic-bezier(0.68, -0.6, 0.32, 1.6);
}
```

```js
// For TRUE spring physics, use Web Animations API (no library needed)
function springAnimate(element, property, targetValue, config = {}) {
  const { stiffness = 180, damping = 12, mass = 1 } = config;
  let current = parseFloat(getComputedStyle(element)[property]) || 0;
  let velocity = 0;

  function step() {
    const displacement = current - targetValue;
    const springForce = -stiffness * displacement;
    const dampingForce = -damping * velocity;
    const acceleration = (springForce + dampingForce) / mass;

    velocity += acceleration * (1 / 60);
    current += velocity * (1 / 60);

    if (Math.abs(velocity) < 0.01 && Math.abs(displacement) < 0.01) {
      current = targetValue;
      element.style[property] = targetValue;
      return;
    }

    element.style[property] = current + 'px';
    requestAnimationFrame(step);
  }

  requestAnimationFrame(step);
}

// Usage: springAnimate(card, 'top', 100, { stiffness: 200, damping: 15 });
```

**Browser compat:** Web Animations API — Chrome 84+, Firefox 48+, Safari 13.1+.
**Performance:** `requestAnimationFrame` for JS springs. For CSS springs, they're just `cubic-bezier` — zero overhead.
**When to use:** Modal open/close, drawer slides, card interactions, any element that should feel "alive."

---

### 3.3 Staggered Animations for Lists/Grids

```css
/* CSS custom properties for stagger timing */
.stagger-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 24px;
}

.stagger-grid .item {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}

.stagger-grid.in-view .item {
  opacity: 1;
  transform: translateY(0);
}

/* Stagger delay via CSS custom properties (most elegant) */
.stagger-grid .item:nth-child(1) { transition-delay: calc(var(--stagger-base, 0.08s) * 1); }
.stagger-grid .item:nth-child(2) { transition-delay: calc(var(--stagger-base, 0.08s) * 2); }
.stagger-grid .item:nth-child(3) { transition-delay: calc(var(--stagger-base, 0.08s) * 3); }
.stagger-grid .item:nth-child(4) { transition-delay: calc(var(--stagger-base, 0.08s) * 4); }
.stagger-grid .item:nth-child(5) { transition-delay: calc(var(--stagger-base, 0.08s) * 5); }
.stagger-grid .item:nth-child(6) { transition-delay: calc(var(--stagger-base, 0.08s) * 6); }
```

```js
// Dynamic stagger via JS — set delays programmatically
function initStaggerGrid(selector, staggerDelay = 80) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const items = entry.target.querySelectorAll('.item');
        items.forEach((item, i) => {
          item.style.transitionDelay = `${i * staggerDelay}ms`;
          item.classList.add('in-view');
        });
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  document.querySelectorAll(selector).forEach(grid => observer.observe(grid));
}
```

**Browser compat:** All browsers.
**Performance:** Stagger delays create cascading transitions — each is lightweight. For grids > 20 items, reduce max stagger count and cap delay.
**When to use:** Project grid, skills list, testimonials, any repeating element group.

---

### 3.4 Scroll-Triggered Animation Sequences

**Technique:** Chain animations so that scrolling through one section triggers a sequence of effects.

```css
/* Timeline-style: elements animate in sequence as you scroll */
.scroll-sequence .step {
  position: sticky;
  top: 20vh;
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}

.scroll-sequence .step.active {
  opacity: 1;
  transform: translateY(0);
}
```

```js
// Create a scroll-driven sequence
function initScrollSequence(container) {
  const steps = container.querySelectorAll('.step');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
      } else {
        // Remove when out of view for re-triggering
        entry.target.classList.remove('active');
      }
    });
  }, {
    threshold: 0.5, // trigger when 50% visible
    rootMargin: '-10% 0px -10% 0px'
  });

  steps.forEach(step => observer.observe(step));
}
```

**Browser compat:** All browsers.
**Performance:** Same as Intersection Observer patterns. Each step is independent.
**When to use:** Process/steps section, feature walkthrough, story-telling sections.

---

## 4. Cinematic Premium Feel

### 4.1 Full-Screen Hero with Video/Image Background

```css
.hero-fullscreen {
  position: relative;
  height: 100vh;
  width: 100%;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Video background */
.hero-fullscreen video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 0;
}

/* Overlay gradient for text readability */
.hero-fullscreen::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.3) 0%,
    rgba(0, 0, 0, 0.6) 100%
  );
  z-index: 1;
}

.hero-fullscreen .hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  color: white;
}
```

```html
<video autoplay muted loop playsinline poster="hero-poster.jpg">
  <source src="hero-video.webm" type="video/webm">
  <source src="hero-video.mp4" type="video/mp4">
</video>
```

```js
// Lazy-load video, prefer poster on mobile
function initHeroVideo() {
  const video = document.querySelector('.hero-fullscreen video');
  if (!video) return;

  // Don't autoplay heavy video on mobile
  if (window.innerWidth < 768) {
    video.removeAttribute('autoplay');
    video.pause();
  }
}
```

**Browser compat:** `<video>` — all browsers. `object-fit: cover` — Chrome 32+, Firefox 32+, Safari 10+.
**Performance:** Video is the most expensive element on a page. Always: `autoplay muted loop playsinline`. Use WebM over MP4 (smaller). Keep hero video < 5MB. Add `poster` as fallback. On mobile, consider image-only.
**When to use:** Homepage hero, landing page splash. NOT for every page.

---

### 4.2 Horizontal Scroll Sections

**Technique:** Transform vertical scroll into horizontal movement using CSS `position: sticky` + JS.

```css
.horizontal-scroll-wrapper {
  height: 300vh; /* Creates scroll distance for horizontal movement */
  position: relative;
}

.horizontal-track {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow: hidden;
  display: flex;
  align-items: center;
}

.horizontal-inner {
  display: flex;
  gap: 4vw;
  padding: 0 5vw;
  will-change: transform;
  transition: none; /* JS controls transform directly */
}

.horizontal-inner .panel {
  flex: 0 0 80vw;
  height: 70vh;
  border-radius: 16px;
  overflow: hidden;
}
```

```js
function initHorizontalScroll() {
  const wrapper = document.querySelector('.horizontal-scroll-wrapper');
  const track = wrapper.querySelector('.horizontal-track');
  const inner = wrapper.querySelector('.horizontal-inner');

  if (!wrapper || !inner) return;

  // Calculate total scroll distance
  const totalWidth = inner.scrollWidth - window.innerWidth;

  window.addEventListener('scroll', () => {
    requestAnimationFrame(() => {
      const rect = wrapper.getBoundingClientRect();
      const wrapperHeight = wrapper.offsetHeight;
      const scrollableDistance = wrapperHeight - window.innerHeight;

      if (rect.top <= 0 && rect.bottom >= window.innerHeight) {
        // We're in the sticky zone
        const progress = Math.abs(rect.top) / scrollableDistance;
        const clampedProgress = Math.max(0, Math.min(1, progress));
        inner.style.transform = `translateX(${-clampedProgress * totalWidth}px)`;
      }
    });
  }, { passive: true });
}
```

**Browser compat:** All browsers. `position: sticky` — Chrome 56+, Firefox 59+, Safari 13+.
**Performance:** `transform: translateX()` is GPU-composited. The scroll listener needs `requestAnimationFrame` throttle. Consider reducing panel complexity if many are in DOM.
**When to use:** Portfolio showcase (projects slide horizontally), skills/tools showcase, timeline/history section.

---

### 4.3 Text Scramble / Typewriter Effects

```css
/* Typewriter cursor blink */
.typewriter {
  border-right: 3px solid currentColor;
  animation: blink-cursor 0.8s step-end infinite;
}

@keyframes blink-cursor {
  from, to { border-color: transparent; }
  50%      { border-color: currentColor; }
}

/* Glitch text effect */
.glitch-text {
  position: relative;
}

.glitch-text::before,
.glitch-text::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
}

.glitch-text::before {
  animation: glitch-1 2s infinite linear alternate-reverse;
  clip-path: polygon(0 0, 100% 0, 100% 45%, 0 45%);
  color: #ff00ff;
}

.glitch-text::after {
  animation: glitch-2 3s infinite linear alternate-reverse;
  clip-path: polygon(0 60%, 100% 60%, 100% 100%, 0 100%);
  color: #00ffff;
}

@keyframes glitch-1 {
  0%, 95% { transform: translate(0); }
  96%     { transform: translate(-2px, 1px); }
  97%     { transform: translate(2px, -1px); }
  98%     { transform: translate(-1px, 2px); }
  99%     { transform: translate(1px, -2px); }
  100%    { transform: translate(0); }
}

@keyframes glitch-2 {
  0%, 93%  { transform: translate(0); }
  94%      { transform: translate(3px, -1px); }
  95%      { transform: translate(-3px, 2px); }
  96%      { transform: translate(2px, -3px); }
  97%      { transform: translate(-1px, 1px); }
  100%     { transform: translate(0); }
}
```

```js
// Typewriter effect
function typewriter(element, text, speed = 50) {
  element.textContent = '';
  element.classList.add('typewriter');
  let i = 0;

  function type() {
    if (i < text.length) {
      element.textContent += text.charAt(i);
      i++;
      setTimeout(type, speed);
    } else {
      // Optionally remove cursor after typing
      // setTimeout(() => element.classList.remove('typewriter'), 2000);
    }
  }
  type();
}

// Text scramble effect (matrix-like reveal)
function scrambleText(element, finalText, duration = 1000) {
  const chars = '!@#$%^&*()_+-=[]{}|;:,.<>?/~`ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  const frames = Math.ceil(duration / 30);
  let frame = 0;

  function update() {
    frame++;
    const progress = frame / frames;
    let result = '';

    for (let i = 0; i < finalText.length; i++) {
      if (finalText[i] === ' ') {
        result += ' ';
      } else if (Math.random() < progress) {
        result += finalText[i];
      } else {
        result += chars[Math.floor(Math.random() * chars.length)];
      }
    }

    element.textContent = result;

    if (frame < frames) {
      requestAnimationFrame(update);
    } else {
      element.textContent = finalText; // Ensure exact final text
    }
  }

  update();
}

// Usage:
// scrambleText(document.querySelector('.hero-title'), 'LYID Web Development');
```

**Browser compat:** All browsers. Pure CSS + vanilla JS.
**Performance:** Typewriter: `textContent` manipulation is lightweight. Scramble: `requestAnimationFrame` at 30fps is trivial. `clip-path` for glitch: GPU-composited.
**When to use:** Hero headline, about section intro, skill names reveal.

---

### 4.4 Cursor Custom Animations

```css
/* Custom cursor dot + follower */
.cursor-dot {
  width: 8px;
  height: 8px;
  background: white;
  border-radius: 50%;
  position: fixed;
  pointer-events: none;
  z-index: 9999;
  mix-blend-mode: difference;
  transition: transform 0.1s ease;
}

.cursor-follower {
  width: 40px;
  height: 40px;
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-radius: 50%;
  position: fixed;
  pointer-events: none;
  z-index: 9998;
  transition: transform 0.3s ease-out, width 0.3s ease, height 0.3s ease, border-color 0.3s ease;
  transform: translate(-50%, -50%);
}

/* Hover state — grow follower */
.cursor-follower.hovering {
  width: 60px;
  height: 60px;
  border-color: rgba(255, 255, 255, 0.8);
}

/* Click state */
.cursor-dot.clicking {
  transform: translate(-50%, -50%) scale(0.5);
}
```

```js
function initCustomCursor() {
  const dot = document.querySelector('.cursor-dot');
  const follower = document.querySelector('.cursor-follower');
  if (!dot || !follower) return;

  let mouseX = 0, mouseY = 0;
  let followerX = 0, followerY = 0;

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    dot.style.left = mouseX + 'px';
    dot.style.top = mouseY + 'px';
  });

  // Smooth follower with lerp
  function animateFollower() {
    followerX += (mouseX - followerX) * 0.1;
    followerY += (mouseY - followerY) * 0.1;
    follower.style.left = followerX + 'px';
    follower.style.top = followerY + 'px';
    requestAnimationFrame(animateFollower);
  }
  animateFollower();

  // Hover effects on interactive elements
  document.querySelectorAll('a, button, .tilt-card, [data-cursor-hover]').forEach(el => {
    el.addEventListener('mouseenter', () => follower.classList.add('hovering'));
    el.addEventListener('mouseleave', () => follower.classList.remove('hovering'));
  });

  // Hide default cursor on desktop
  if (window.matchMedia('(pointer: fine)').matches) {
    document.body.style.cursor = 'none';
    document.querySelectorAll('a, button').forEach(el => el.style.cursor = 'none');
  }
}

document.addEventListener('DOMContentLoaded', initCustomCursor);
```

```html
<div class="cursor-dot"></div>
<div class="cursor-follower"></div>
```

**Browser compat:** All browsers. Only show on desktop (check `pointer: fine`).
**Performance:** Two `requestAnimationFrame` loops — minimal overhead. `left`/`top` on cursor is fine since elements are tiny. Don't use `will-change` on cursor elements (too many repaints from position changes).
**When to use:** Desktop only. Creative/portfolio sites. Hide on mobile/touch devices.

---

### 4.5 Smooth Page Transitions

**Technique:** View Transitions API (native) or overlay-based transitions (cross-browser).

```css
/* View Transitions API — native cross-page transitions */
@view-transition {
  navigation: auto;
}

::view-transition-old(root) {
  animation: fade-out 0.3s ease-out forwards;
}

::view-transition-new(root) {
  animation: fade-in 0.3s ease-out forwards;
}

@keyframes fade-out {
  from { opacity: 1; }
  to   { opacity: 0; }
}

@keyframes fade-in {
  from { opacity: 0; }
  to   { opacity: 1; }
}

/* Named transitions for specific elements */
.hero-image {
  view-transition-name: hero;
}

/* Cross-browser fallback — overlay transition */
.page-transition-overlay {
  position: fixed;
  inset: 0;
  background: #000;
  z-index: 10000;
  transform: scaleY(0);
  transform-origin: bottom;
  pointer-events: none;
}

.page-transition-overlay.active {
  animation: overlay-in 0.5s cubic-bezier(0.77, 0, 0.175, 1) forwards,
             overlay-out 0.5s cubic-bezier(0.77, 0, 0.175, 1) 0.5s forwards;
}

@keyframes overlay-in {
  from { transform: scaleY(0); transform-origin: bottom; }
  to   { transform: scaleY(1); transform-origin: bottom; }
}

@keyframes overlay-out {
  from { transform: scaleY(1); transform-origin: top; }
  to   { transform: scaleY(0); transform-origin: top; }
}
```

```js
// View Transitions API — works on same-origin navigation
document.querySelectorAll('a[href]').forEach(link => {
  link.addEventListener('click', async (e) => {
    e.preventDefault();
    const href = link.getAttribute('href');

    if (document.startViewTransition) {
      const transition = document.startViewTransition(() => {
        window.location.href = href;
      });
    } else {
      // Fallback: simple overlay
      const overlay = document.querySelector('.page-transition-overlay');
      overlay.classList.add('active');
      setTimeout(() => { window.location.href = href; }, 500);
    }
  });
});
```

**Browser compat:** View Transitions API — Chrome 111+, Edge 111+. NOT Firefox, NOT Safari (as of 2024). Fallback approach: all browsers.
**Performance:** View Transitions: zero overhead (browser-native). Overlay: minimal (one CSS animation).
**When to use:** Multi-page portfolio sites. Single-page apps don't need this (use route transitions instead).

---

### 4.6 Loading Animations

```css
/* Premium preloader */
.preloader {
  position: fixed;
  inset: 0;
  background: #0a0a0a;
  z-index: 10001;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity 0.6s ease-out, visibility 0.6s;
}

.preloader.hidden {
  opacity: 0;
  visibility: hidden;
}

/* Morphing text preloader */
.preloader-text {
  font-size: 3rem;
  font-weight: 700;
  color: white;
  letter-spacing: 0.2em;
}

/* Spinning ring */
.loader-ring {
  width: 50px;
  height: 50px;
  border: 2px solid rgba(255, 255, 255, 0.1);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Progress bar at top */
.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: linear-gradient(90deg, #00f5ff, #ff00ff);
  z-index: 10001;
  transform-origin: left;
  transform: scaleX(0);
  transition: transform 0.3s ease-out;
}
```

```js
// Preloader with animated text
function initPreloader() {
  const preloader = document.querySelector('.preloader');
  const textEl = document.querySelector('.preloader-text');
  const text = 'LYID';

  // Scramble reveal
  scrambleText(textEl, text, 800);

  window.addEventListener('load', () => {
    setTimeout(() => {
      preloader.classList.add('hidden');
    }, 1200); // Show for at least 1.2s
  });
}

// Page load progress bar
function initProgressBar() {
  const bar = document.querySelector('.progress-bar');
  if (!bar) return;

  let progress = 0;
  const interval = setInterval(() => {
    progress += Math.random() * 15;
    if (progress >= 90) {
      clearInterval(interval);
      progress = 90;
    }
    bar.style.transform = `scaleX(${progress / 100})`;
  }, 100);

  window.addEventListener('load', () => {
    clearInterval(interval);
    bar.style.transform = 'scaleX(1)';
    setTimeout(() => {
      bar.style.opacity = '0';
    }, 500);
  });
}
```

**Browser compat:** All browsers. Pure CSS + JS.
**Performance:** Preloader is fixed-position overlay — minimal rendering cost. Remove from DOM after hide transition to free memory.
**When to use:** Every page should have a subtle loading indicator. Full preloader for homepage only.

---

## 5. Modern CSS APIs

### 5.1 Scroll-Driven Animations (CSS `animation-timeline`)

**The future of scroll animations — pure CSS, no JavaScript.**

```css
/* Progress bar that fills as you scroll */
.scroll-progress {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: linear-gradient(90deg, #00f5ff, #ff00ff);
  transform-origin: left;
  transform: scaleX(0);
  animation: grow-progress linear both;
  animation-timeline: scroll();
}

@keyframes grow-progress {
  to { transform: scaleX(1); }
}

/* Fade-in on scroll — pure CSS */
.scroll-fade-in {
  animation: scroll-fade linear both;
  animation-timeline: view();
  animation-range: entry 0% cover 40%;
}

@keyframes scroll-fade {
  from { opacity: 0; transform: translateY(60px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* Horizontal movement on scroll */
.scroll-pan {
  animation: scroll-pan linear both;
  animation-timeline: view();
  animation-range: entry 0% exit 100%;
}

@keyframes scroll-pan {
  from { transform: translateX(-50px); }
  to   { transform: translateX(50px); }
}

/* Named scroll timeline for specific scroller */
.scroller-container {
  scroll-timeline-name: --section-scroll;
  scroll-timeline-axis: block;
}

.scroller-child {
  animation: fade-in linear both;
  animation-timeline: --section-scroll;
}

/* View timeline — trigger when element enters view */
.reveal-on-view {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 10% cover 30%;
  animation-fill-mode: both;
}

@keyframes reveal {
  from {
    opacity: 0;
    transform: translateY(80px) scale(0.95);
    filter: blur(4px);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
    filter: blur(0);
  }
}
```

**Browser compat:** Chrome 115+, Edge 115+, Safari 18.2+. **NOT Firefox** (as of 2024). Use `@supports (animation-timeline: scroll())` for progressive enhancement.
**Performance:** Offloaded to the browser's compositor thread — zero JavaScript overhead. The most performant scroll animation approach possible.
**When to use:** Progressive enhancement for Chrome/Safari users. Always provide JS fallback for Firefox.

---

### 5.2 View Transitions API

```css
/* Cross-document view transitions */
@view-transition {
  navigation: auto;
}

/* Default transition */
::view-transition-old(root) {
  animation: slide-out 0.3s ease-in forwards;
}

::view-transition-new(root) {
  animation: slide-in 0.3s ease-out forwards;
}

@keyframes slide-out {
  to { opacity: 0; transform: scale(0.95); filter: blur(4px); }
}

@keyframes slide-in {
  from { opacity: 0; transform: scale(1.05); filter: blur(4px); }
}

/* Match hero image across pages */
.hero-image { view-transition-name: hero; }

::view-transition-old(hero) {
  animation: fade-scale-out 0.5s ease-in forwards;
}

::view-transition-new(hero) {
  animation: fade-scale-in 0.5s ease-out forwards;
}

@keyframes fade-scale-out {
  to { opacity: 0; transform: scale(1.1); }
}

@keyframes fade-scale-in {
  from { opacity: 0; transform: scale(0.9); }
}

/* Preserve nav across page transitions */
.site-nav { view-transition-name: nav; }
```

```js
// Programmatic view transitions (SPA-like)
async function navigateTo(url) {
  if (!document.startViewTransition) {
    window.location.href = url;
    return;
  }

  const response = await fetch(url);
  const html = await response.text();

  document.startViewTransition(() => {
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    document.body.innerHTML = doc.body.innerHTML;
    document.head.innerHTML = doc.head.innerHTML;
  });
}
```

**Browser compat:** Chrome 111+, Edge 111+. NOT Firefox, NOT Safari (check caniuse for updates).
**When to use:** Multi-page portfolio site navigation. Always with fallback.

---

### 5.3 CSS linear() for Complex Easing

```css
/* Custom spring-like bounce using linear() */
.bounce-ease {
  animation-timing-function: linear(
    0, 0.004, 0.016, 0.035, 0.063, 0.098, 0.141, 0.191,
    0.25, 0.316, 0.391, 0.473, 0.563, 0.661, 0.766, 0.879,
    1, 0.934, 0.879, 0.837, 0.807, 0.789, 0.784, 0.79,
    0.808, 0.837, 0.877, 0.928, 0.989, 1.059, 1.138, 1.225,
    1.319, 1.42, 1.526, 1.636, 1.748, 1.86, 1.971, 2.079,
    2.181, 2.275, 2.359, 2.432, 2.493, 2.542, 2.578, 2.601,
    2.612, 2.612, 2.601, 2.578, 2.542, 2.493, 2.432, 2.359,
    2.275, 2.181, 2.079, 1.971, 1.86, 1.748, 1.636, 1.526,
    1.42, 1.319, 1.225, 1.138, 1.059, 1, 0.989, 0.979, 0.962,
    0.958, 0.95, 0.957, 0.97, 0.983, 1, 1.017, 1.015, 1.025
  );
}

/* Smooth snap to grid */
.snap-ease {
  animation-timing-function: linear(
    0 0%, 0.0027 1%, 0.0113 2.5%, 0.0475 5.75%, 0.111 8.5%,
    0.197 11.25%, 0.539 18.5%, 0.696 23%, 0.775 26%,
    0.856 29.75%, 0.906 32.5%, 0.939 35%, 1 42.5%,
    0.981 47.5%, 0.97 52.5%, 0.97 57.5%, 1 72.5%,
    0.999 85%, 1 100%
  );
}
```

**Browser compat:** Chrome 113+, Firefox 112+, Safari 17.2+. Good support.
**When to use:** Anywhere you need a complex easing curve that cubic-bezier can't express (bounces, multi-stage easing).

---

## 6. Performance Bible

### The Non-Negotiable Rules

```
1. ONLY animate transform and opacity → GPU-composited, 60fps
2. NEVER animate: top, left, width, height, margin, padding → triggers layout/paint
3. Use will-change: transform on elements about to animate → promotes to own layer
4. Remove will-change after animation completes → frees GPU memory
5. Use requestAnimationFrame for JS-driven animations → syncs with display refresh
6. Use { passive: true } on scroll/wheel/touch event listeners → doesn't block scroll
7. Use Intersection Observer over scroll events → async, non-blocking, 0 cost when idle
8. Debounce/throttle expensive handlers → never more than 60 callbacks/sec
9. Test on mid-range mobile → if it's smooth there, it's smooth everywhere
10. Reduce motion: respect prefers-reduced-motion → accessibility requirement
```

### prefers-reduced-motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### Performance Budget per Technique

| Technique | GPU Cost | CPU Cost | Mobile OK? |
|-----------|----------|----------|------------|
| `transform` animations | Low | None | ✅ |
| `opacity` fade | Low | None | ✅ |
| `clip-path` (polygon) | Medium | Low | ✅ |
| Parallax (2 layers) | Low | Low | ✅ |
| Parallax (5+ layers) | Medium | Medium | ⚠️ |
| Ken Burns | Low | None | ✅ |
| Video background | High | Medium | ⚠️ (use poster) |
| Tilt (3D) | Medium | Low | ✅ |
| Text scramble | None | Low | ✅ |
| Canvas animation | High | High | ⚠️ |
| Scroll listeners (unthrottled) | None | High | ❌ |

---

## 7. Libraries Reference

### GSAP (GreenSock Animation Platform)

```html
<!-- CDN — free for non-commercial, license needed for commercial -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
```

```js
// GSAP ScrollTrigger — industry standard
gsap.registerPlugin(ScrollTrigger);

// Fade up on scroll
gsap.from('.fade-up', {
  scrollTrigger: {
    trigger: '.fade-up',
    start: 'top 85%',
    end: 'top 20%',
    toggleActions: 'play none none reverse'
  },
  y: 60,
  opacity: 0,
  duration: 1,
  ease: 'power3.out'
});

// Parallax image
gsap.to('.parallax-img', {
  scrollTrigger: {
    trigger: '.parallax-section',
    start: 'top bottom',
    end: 'bottom top',
    scrub: true
  },
  y: -100,
  ease: 'none'
});

// Stagger grid items
gsap.from('.grid-item', {
  scrollTrigger: {
    trigger: '.grid',
    start: 'top 80%'
  },
  y: 80,
  opacity: 0,
  duration: 0.8,
  stagger: 0.1,
  ease: 'power3.out'
});

// Horizontal scroll
gsap.to('.horizontal-inner', {
  x: () => -(document.querySelector('.horizontal-inner').scrollWidth - window.innerWidth),
  ease: 'none',
  scrollTrigger: {
    trigger: '.horizontal-wrapper',
    start: 'top top',
    end: 'bottom bottom',
    scrub: 1,
    pin: true
  }
});

// Text split and animate
gsap.from('.hero-title .word', {
  y: 80,
  opacity: 0,
  duration: 1,
  stagger: 0.05,
  ease: 'power4.out',
  delay: 0.5
});
```

**License:** Free for non-commercial. Commercial: $99+/year.
**Bundle size:** ~30KB minified (core + ScrollTrigger).
**When to use:** Complex sequences, pinned sections, scrubbed scroll animations, anything beyond basic fade-in.

### Locomotive Scroll (locomotivemtl)

```html
<link rel="stylesheet" href="https://unpkg.com/locomotive-scroll/dist/locomotive-scroll.min.css">
<script src="https://unpkg.com/locomotive-scroll/dist/locomotive-scroll.min.js"></script>
```

```html
<!-- Locomotive wraps everything in a smooth-scroll container -->
<div data-scroll-container>
  <div data-scroll-section>
    <div data-scroll data-scroll-speed="2">Fast layer</div>
    <div data-scroll data-scroll-speed="0.5">Slow layer</div>
    <div data-scroll data-scroll-speed="-1">Reverse layer</div>
  </div>
</div>
```

```js
const scroll = new LocomotiveScroll({
  el: document.querySelector('[data-scroll-container]'),
  smooth: true,
  multiplier: 1,
  lerp: 0.1 // smooth interpolation
});

// Parallax is declarative via HTML attributes
// data-scroll-speed: higher = moves more relative to scroll
// data-scroll-direction: "horizontal" for horizontal sections
// data-scroll-delay: "0.1" for delayed parallax
```

**Status:** Locomotive Scroll v4+ is unmaintained. Use locomotive-scroll for smooth scrolling only, not for new projects. Prefer GSAP ScrollTrigger for scroll animations.
**When to use:** Legacy projects only. New projects → GSAP ScrollTrigger or native Intersection Observer.

### Lenis (Smooth Scroll - Locomotive successor)

```html
<script src="https://unpkg.com/lenis@1.1.14/dist/lenis.min.js"></script>
```

```js
const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smoothWheel: true
});

// Sync with GSAP
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((time) => {
  lenis.raf(time * 1000);
});
gsap.ticker.lagSmoothing(0);

function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}
requestAnimationFrame(raf);
```

**When to use:** Add smooth scrolling to any site. Pairs perfectly with GSAP ScrollTrigger. ~7KB minified.

---

## 8. Implementation Priority for LYID Portfolio

### Phase 1 — Immediate Impact (Week 1)
1. ✅ **Intersection Observer fade-up** on all sections → biggest ROI
2. ✅ **Ken Burns** on hero image → instant premium feel
3. ✅ **Staggered grid animation** on projects section
4. ✅ **Progress bar** at top of page on scroll
5. ✅ **`prefers-reduced-motion`** media query

### Phase 2 — Polish (Week 2)
6. ✅ **Parallax** on hero section (1-2 layers only)
7. ✅ **Text reveal** (split + slide-up) on headlines
8. ✅ **Tilt** on project cards
9. ✅ **Custom cursor** (desktop only)
10. ✅ **Loading animation** (text scramble preloader)

### Phase 3 — Premium Feel (Week 3)
11. ✅ **Horizontal scroll** section for projects/tools
12. ✅ **clip-path reveal** on section images
13. ✅ **Lenis smooth scroll** integration
14. ✅ **Scroll-driven animations** with `animation-timeline` (progressive enhancement)
15. ✅ **View Transitions** for page navigation (if multi-page)

### Recommended Easing Values (Copy-Paste)

```css
:root {
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-snap: cubic-bezier(0.85, 0, 0.15, 1);
  --duration-fast: 0.3s;
  --duration-normal: 0.6s;
  --duration-slow: 1s;
  --duration-reveal: 0.8s;
}
```

### Minimal Code Structure

```
portfolio/
├── index.html
├── css/
│   ├── base.css          # Reset, typography, colors
│   ├── animations.css    # All animation classes (fade-up, reveal, etc.)
│   └── responsive.css    # Mobile adjustments, reduced motion
├── js/
│   ├── main.js           # Init all animations, intersection observers
│   ├── cursor.js         # Custom cursor (optional, desktop only)
│   └── preloader.js      # Loading screen
└── assets/
    └── images/           # Optimized, WebP preferred
```

---

## Sources & Inspiration

### Awwwards-Winning Patterns
- Apple product pages (scroll-scrubbed canvas animations)
- Locomotive.co (smooth scroll + parallax)
- Monopo London (horizontal scroll + text reveals)
- Bruno Simon (WebGL + scroll integration)
- Active Theory (custom cursor + particle effects)

### Key Articles
- CSS-Tricks: "Fancy Scrolling Animations on Apple Product Pages" (May 2020)
- Chrome DevRel: "Scroll-driven Animations" (animation-timeline docs)
- MDN: animation-timeline, View Transitions API
- GSAP Docs: ScrollTrigger patterns and demos
- Can I Use: animation-timeline, View Transitions

### CodePen References
- Search: "GSAP ScrollTrigger parallax" → hundreds of working examples
- Search: "pure CSS Ken Burns" → multiple implementations
- Search: "intersection observer fade in" → vanilla JS patterns
- Search: "text scramble effect" → various JS implementations

---

*Last updated: July 2026*
