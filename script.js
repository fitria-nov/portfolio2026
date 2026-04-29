// Theme
function setTheme(t){document.documentElement.setAttribute('data-theme',t);localStorage.setItem('theme',t);const s=document.getElementById('themeToggleSm');if(s)s.textContent=t==='dark'?'☀️':'🌙'}
setTheme(localStorage.getItem('theme')||'dark');
document.getElementById('themeToggle').addEventListener('click',()=>{const c=document.documentElement.getAttribute('data-theme');setTheme(c==='dark'?'light':'dark')});
document.getElementById('themeToggleSm').addEventListener('click',()=>{const c=document.documentElement.getAttribute('data-theme');setTheme(c==='dark'?'light':'dark')});

// Navigation with staggered animation
function navigateTo(section){
  document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
  const panel=document.getElementById(section);
  if(panel){
    panel.classList.add('active');
    window.scrollTo(0,0);
    // Reset and trigger staggered animations
    animatePanel(panel);
  }
  const nav=document.querySelector(`.nav-item[data-section="${section}"]`);
  if(nav)nav.classList.add('active');
  document.getElementById('sidebar').classList.remove('open');
}

function animatePanel(panel){
  const items=panel.querySelectorAll('.anim,.anim-left,.anim-scale');
  items.forEach(el=>el.classList.remove('show'));
  items.forEach((el,i)=>{
    setTimeout(()=>el.classList.add('show'), 60+i*70);
  });
  // Animate skill bars if in skills panel
  panel.querySelectorAll('.sb-fill').forEach(bar=>{
    const w=bar.style.width;bar.style.width='0';
    setTimeout(()=>{bar.style.width=w},300);
  });
}

document.querySelectorAll('.nav-item').forEach(i=>{i.addEventListener('click',e=>{e.preventDefault();navigateTo(i.dataset.section)})});
document.getElementById('menuBtn').addEventListener('click',()=>{document.getElementById('sidebar').classList.toggle('open')});
document.getElementById('main').addEventListener('click',()=>{document.getElementById('sidebar').classList.remove('open')});
document.querySelectorAll('a[href="#contact"]').forEach(a=>{a.addEventListener('click',e=>{e.preventDefault();navigateTo('contact')})});

// Initial animation for overview
window.addEventListener('DOMContentLoaded',()=>{
  const overview=document.getElementById('overview');
  if(overview) animatePanel(overview);

  // Project filters
  document.querySelectorAll('.proj-filter').forEach(btn=>{
    btn.addEventListener('click',()=>{
      document.querySelectorAll('.proj-filter').forEach(b=>b.classList.remove('active'));
      btn.classList.add('active');
      const filter=btn.dataset.filter;
      const cards=document.querySelectorAll('.proj-card');
      cards.forEach(card=>{
        card.classList.remove('show','hidden');
        card.style.opacity='0';
        card.style.transform='translateY(20px)';
      });
      let visibleIdx=0;
      cards.forEach(card=>{
        if(filter==='all'||card.dataset.category===filter){
          card.classList.remove('hidden');
          setTimeout(()=>{
            card.style.opacity='1';
            card.style.transform='translateY(0)';
            card.classList.add('show');
          },60+visibleIdx*100);
          visibleIdx++;
        } else {
          card.classList.add('hidden');
        }
      });
    });
  });
});

// Greeting
const hour=new Date().getHours();
const greetEl=document.getElementById('greeting');
if(greetEl){
  let g='Good Evening';
  if(hour>=5&&hour<12)g='Good Morning';
  else if(hour>=12&&hour<17)g='Good Afternoon';
  else if(hour>=17&&hour<21)g='Good Evening';
  greetEl.textContent=g;
}

// Typing
const typedEl=document.getElementById('typed');
const phrases=['elegant web experiences','intuitive UI/UX designs','full-stack applications','SEO-optimized content','digital products that matter'];
let pIdx=0,cIdx=0,del=false;
function typeEffect(){
  if(!typedEl)return;
  const cur=phrases[pIdx];
  if(!del){typedEl.textContent=cur.slice(0,cIdx+1);cIdx++;if(cIdx===cur.length){del=true;setTimeout(typeEffect,2000);return}setTimeout(typeEffect,60)}
  else{typedEl.textContent=cur.slice(0,cIdx-1);cIdx--;if(cIdx===0){del=false;pIdx=(pIdx+1)%phrases.length;setTimeout(typeEffect,400);return}setTimeout(typeEffect,30)}
}
typeEffect();

// Media upload
function handleMedia(input){
  const file=input.files[0];if(!file)return;
  const reader=new FileReader();
  reader.onload=function(e){
    const ph=input.closest('.media-placeholder');
    const grid=ph.parentElement;
    const sm=ph.classList.contains('sm');
    const item=document.createElement('div');
    item.className='media-item'+(sm?' sm':'')+' anim-scale show';
    item.style.animation='pulse .4s ease';
    item.onclick=function(){openLightbox(e.target.result)};
    if(file.type.startsWith('video/')){
      const v=document.createElement('video');v.src=e.target.result;v.style.cssText='width:100%;height:100%;object-fit:cover';v.muted=true;
      v.addEventListener('mouseenter',()=>v.play());v.addEventListener('mouseleave',()=>{v.pause();v.currentTime=0});
      item.appendChild(v);
    }else{const img=document.createElement('img');img.src=e.target.result;img.alt=file.name;item.appendChild(img)}
    const lbl=document.createElement('span');lbl.textContent=file.name.split('.')[0];item.appendChild(lbl);
    grid.insertBefore(item,ph);input.value='';
  };reader.readAsDataURL(file);
}

// Lightbox
function openLightbox(src){const lb=document.getElementById('lightbox');document.getElementById('lightboxImg').src=src;lb.classList.add('open')}
function closeLightbox(){document.getElementById('lightbox').classList.remove('open')}
document.querySelectorAll('.media-item:not(.media-placeholder)').forEach(item=>{item.addEventListener('click',()=>{const img=item.querySelector('img');if(img)openLightbox(img.src)})});

