  document.getElementById('yr').textContent = new Date().getFullYear();
  // scroll reveal
  const io = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
  },{threshold:.12});
  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
  // nav active state
  (function(){
    const nav=document.querySelector('.navlinks');if(!nav)return;
    const links=[...nav.querySelectorAll('a[href^="#"]')];
    const workIds=['thread','work'];
    const obs=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting)links.forEach(l=>l.classList.toggle('active',workIds.includes(e.target.id)?l.getAttribute('href')==='#thread':l.getAttribute('href')==='#'+e.target.id));});},{rootMargin:'-45% 0 -50% 0',threshold:0});
    links.forEach(l=>{const el=document.getElementById(l.getAttribute('href').slice(1));if(el)obs.observe(el);});
    const workEl=document.getElementById('work');if(workEl)obs.observe(workEl);
  })();
