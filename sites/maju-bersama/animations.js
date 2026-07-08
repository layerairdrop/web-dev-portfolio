/* PT Maju Bersama — Cinematic Animations */
(function(){
'use strict';

/* 1. Scroll Progress Bar */
function initProgressBar(){
  var bar=document.querySelector('.progress-bar');
  if(!bar)return;
  window.addEventListener('scroll',function(){
    var h=document.documentElement.scrollHeight-window.innerHeight;
    var p=h>0?window.scrollY/h:0;
    bar.style.transform='scaleX('+p+')';
  },{passive:true});
}

/* 2. Intersection Observer — Fade Up + Stagger + Reveal */
function initFadeUp(){
  var els=document.querySelectorAll('.fade-up,.stagger-item,.reveal-clip,.text-reveal');
  if(!els.length)return;
  var obs=new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){
        e.target.classList.add('visible');
        obs.unobserve(e.target);
      }
    });
  },{threshold:0.12,rootMargin:'0px 0px -40px 0px'});
  els.forEach(function(el){obs.observe(el);});
}

/* 3. Stagger Grid Items */
function initStagger(){
  var grids=document.querySelectorAll('[data-stagger]');
  grids.forEach(function(grid){
    var items=grid.querySelectorAll('.stagger-item');
    items.forEach(function(item,i){
      item.style.transitionDelay=(i*0.08)+'s';
    });
  });
}

/* 4. Tilt Cards (3D Perspective) */
function initTilt(){
  if(window.innerWidth<769)return;
  var cards=document.querySelectorAll('.tilt-card');
  cards.forEach(function(card){
    card.addEventListener('mousemove',function(e){
      var r=card.getBoundingClientRect();
      var x=(e.clientX-r.left)/r.width-0.5;
      var y=(e.clientY-r.top)/r.height-0.5;
      card.style.transform='perspective(800px) rotateY('+(x*8)+'deg) rotateX('+(-y*8)+'deg) scale(1.02)';
    });
    card.addEventListener('mouseleave',function(){
      card.style.transform='perspective(800px) rotateY(0) rotateX(0) scale(1)';
    });
  });
}

/* 5. Custom Cursor */
function initCursor(){
  if(window.innerWidth<769||matchMedia('(pointer:coarse)').matches)return;
  var cursor=document.createElement('div');
  cursor.className='custom-cursor';
  document.body.appendChild(cursor);
  var mx=0,my=0,cx=0,cy=0;
  document.addEventListener('mousemove',function(e){mx=e.clientX;my=e.clientY;});
  function animate(){
    cx+=(mx-cx)*0.15;
    cy+=(my-cy)*0.15;
    cursor.style.transform='translate('+(cx-10)+'px,'+(cy-10)+'px)';
    requestAnimationFrame(animate);
  }
  animate();
  var targets=document.querySelectorAll('a,button,.service-card,.product-card,.why-card,.tilt-card');
  targets.forEach(function(t){
    t.addEventListener('mouseenter',function(){cursor.classList.add('hover');});
    t.addEventListener('mouseleave',function(){cursor.classList.remove('hover');});
  });
}

/* 6. Parallax Hero */
function initParallax(){
  var layers=document.querySelectorAll('.parallax-layer');
  if(!layers.length)return;
  window.addEventListener('scroll',function(){
    var y=window.pageYOffset;
    layers.forEach(function(l){
      var speed=parseFloat(l.dataset.speed)||0.3;
      l.style.transform='translateY('+(y*speed)+'px)';
    });
  },{passive:true});
}

/* 7. Smooth Anchor Links */
function initSmoothScroll(){
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click',function(e){
      var target=document.querySelector(a.getAttribute('href'));
      if(target){
        e.preventDefault();
        target.scrollIntoView({behavior:'smooth',block:'start'});
      }
    });
  });
}

/* Init All */
document.addEventListener('DOMContentLoaded',function(){
  initProgressBar();
  initFadeUp();
  initStagger();
  initTilt();
  initCursor();
  initParallax();
  initSmoothScroll();
});

})();
