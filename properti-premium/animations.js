/* Properti Premium — Cinematic Animations */
(function(){
'use strict';

function initProgressBar(){
  var bar=document.querySelector('.progress-bar');
  if(!bar)return;
  window.addEventListener('scroll',function(){
    var h=document.documentElement.scrollHeight-window.innerHeight;
    bar.style.transform='scaleX('+(h>0?window.scrollY/h:0)+')';
  },{passive:true});
}

function initReveal(){
  var els=document.querySelectorAll('.fade-up,.stagger-item,.reveal-clip');
  if(!els.length)return;
  var obs=new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){e.target.classList.add('visible');obs.unobserve(e.target);}
    });
  },{threshold:.1,rootMargin:'0px 0px -40px 0px'});
  els.forEach(function(el){obs.observe(el);});
}

function initStagger(){
  document.querySelectorAll('[data-stagger]').forEach(function(g){
    g.querySelectorAll('.stagger-item').forEach(function(el,i){
      el.style.transitionDelay=(i*.08)+'s';
    });
  });
}

function initTilt(){
  if(window.innerWidth<769)return;
  document.querySelectorAll('.tilt-card').forEach(function(card){
    card.addEventListener('mousemove',function(e){
      var r=card.getBoundingClientRect();
      var x=(e.clientX-r.left)/r.width-.5;
      var y=(e.clientY-r.top)/r.height-.5;
      card.style.transform='perspective(800px) rotateY('+(x*6)+'deg) rotateX('+(-y*6)+'deg)';
    });
    card.addEventListener('mouseleave',function(){
      card.style.transform='perspective(800px) rotateY(0) rotateX(0)';
    });
  });
}

function initCursor(){
  if(window.innerWidth<769||matchMedia('(pointer:coarse)').matches)return;
  var c=document.createElement('div');
  c.className='custom-cursor';
  document.body.appendChild(c);
  var mx=0,my=0,cx=0,cy=0;
  document.addEventListener('mousemove',function(e){mx=e.clientX;my=e.clientY;});
  (function loop(){cx+=(mx-cx)*.15;cy+=(my-cy)*.15;c.style.transform='translate('+(cx-8)+'px,'+(cy-8)+'px)';requestAnimationFrame(loop);})();
  document.querySelectorAll('a,button,.property-card,.tilt-card').forEach(function(t){
    t.addEventListener('mouseenter',function(){c.classList.add('hover');});
    t.addEventListener('mouseleave',function(){c.classList.remove('hover');});
  });
}

function initNav(){
  var nav=document.querySelector('nav');
  var h=document.getElementById('hamburger');
  var links=document.getElementById('navLinks');
  if(nav)window.addEventListener('scroll',function(){nav.classList.toggle('scrolled',window.scrollY>60);},{passive:true});
  if(h&&links){h.addEventListener('click',function(){links.classList.toggle('open');});links.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){links.classList.remove('open');});});}
}

function initAccordion(){
  document.querySelectorAll('.accordion-btn').forEach(function(btn){
    btn.addEventListener('click',function(){
      var panel=btn.nextElementSibling;
      var isOpen=panel.style.maxHeight;
      document.querySelectorAll('.accordion-panel').forEach(function(p){p.style.maxHeight=null;var prev=p.previousElementSibling;prev.classList.remove('active');var ic=prev.querySelector('.accordion-icon');if(ic)ic.style.transform='';});
      if(!isOpen){panel.style.maxHeight=panel.scrollHeight+'px';btn.classList.add('active');var icon=btn.querySelector('.accordion-icon');if(icon)icon.style.transform='rotate(45deg)';}
    });
  });
}

document.addEventListener('DOMContentLoaded',function(){
  initNav();initProgressBar();initReveal();initStagger();initTilt();initCursor();initAccordion();
});
})();
