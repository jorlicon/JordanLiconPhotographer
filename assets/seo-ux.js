(function(){
  function pushEvent(name,data){
    window.dataLayer=window.dataLayer||[];
    window.dataLayer.push(Object.assign({event:name,page_path:location.pathname},data||{}));
  }
  function initMobileMenu(){
    var toggle=document.querySelector('[data-mobile-menu-toggle]');
    var menu=document.querySelector('[data-mobile-menu]');
    if(!toggle||!menu)return;
    var firstLink=menu.querySelector('a');
    function setOpen(open){
      toggle.setAttribute('aria-expanded',String(open));
      toggle.setAttribute('aria-label',open?'Close navigation':'Open navigation');
      menu.hidden=!open;
      document.body.classList.toggle('mobile-menu-open',open);
      if(open&&firstLink)firstLink.focus();
      if(!open)toggle.focus();
    }
    toggle.addEventListener('click',function(){setOpen(toggle.getAttribute('aria-expanded')!=='true');});
    menu.addEventListener('click',function(event){if(event.target.closest('a'))setOpen(false);});
    document.addEventListener('keydown',function(event){if(event.key==='Escape'&&toggle.getAttribute('aria-expanded')==='true')setOpen(false);});
  }
  function addHomepagePath(){
    var lede=document.querySelector('.service-lede');
    if(!lede||document.querySelector('.service-jump'))return;
    var nav=document.createElement('nav');
    nav.className='service-jump';
    nav.setAttribute('aria-label','Photography service paths');
    nav.innerHTML='<a href="#headshots"><span>Headshots</span><span>01</span></a><a href="#architecture"><span>Architecture</span><span>02</span></a><a href="#food"><span>Food and beverage</span><span>03</span></a><a href="#services"><span>Commercial work</span><span>04</span></a><a href="drone-portfolio.html"><span>Drone Photography &amp; Aerial Production</span><span>05</span></a><a href="cinematography.html"><span>Cinematography</span><span>06</span></a><a href="#studio"><span>Studio Photography</span><span>07</span></a><a class="service-jump-inquire" href="#contact"><span>Inquire</span><span>Start here</span></a>';
    lede.insertAdjacentElement('afterend',nav);
  }
  function addTopServiceCards(){
    var grid=document.querySelector('.path-grid');
    if(!grid||grid.querySelector('[data-top-service-card]'))return;
    grid.insertAdjacentHTML('beforeend','<a class="path-card" data-top-service-card href="food-photography-portfolio.html"><div class="path-media"><img src="assets/optimized/blog/food-beverage-storytelling-jordan-licon.jpg" alt="Commercial food and beverage photography in El Paso" width="1400" height="933" loading="lazy"></div><div class="path-copy"><div class="path-num mono">Food and beverage</div><h2>Food images that make dishes <em>stand out</em></h2><p>Restaurant, hospitality, menu, beverage, and campaign photography for brands that need appetizing images with consistent color and polish.</p><span class="blog-link mono">View food portfolio</span></div></a><a class="path-card" data-top-service-card href="drone-portfolio.html"><div class="path-media"><img src="assets/drone/drone-01.jpg" alt="Drone photography and aerial production by Jordan Licon in El Paso" width="1400" height="933" loading="lazy"></div><div class="path-copy"><div class="path-num mono">Drone Photography &amp; Aerial Production</div><h2>Coverage from a <em>wider view</em></h2><p>FAA-certified drone photography and aerial production for architecture, infrastructure, commercial campaigns, and editorial work.</p><span class="blog-link mono">View drone portfolio</span></div></a><a class="path-card" data-top-service-card href="cinematography.html"><div class="path-media"><img src="assets/films/the-reflection-poster.jpeg" alt="Cinematography production by Jordan Licon" width="1400" height="933" loading="lazy"></div><div class="path-copy"><div class="path-num mono">Cinematography</div><h2>Motion with a clear <em>point of view</em></h2><p>Director of photography and commercial film production for brands, agencies, institutions, and editorial projects.</p><span class="blog-link mono">View cinematography</span></div></a>');
  }
  function addArticleGuide(){
    var article=document.querySelector('article');
    var trust=article&&article.querySelector('.author-trust');
    if(!article||!trust||document.querySelector('.article-contents'))return;
    var ids={'What is a Professional Headshot?':'what-is-a-professional-headshot','The 5 Elements of a Great Professional Headshot':'five-elements','How to Choose a Professional Headshot Photographer':'choose-photographer','What to Expect in a Professional Headshot Session':'session','Headshot Costs and Investment':'cost'};
    article.querySelectorAll('h2').forEach(function(heading){var key=heading.textContent.trim();if(ids[key])heading.id=ids[key];});
    var answer=document.createElement('section');
    answer.className='seo-quick-answer';
    answer.setAttribute('aria-labelledby','quick-answer-title');
    answer.innerHTML='<h2 id="quick-answer-title">The short answer</h2><p>A strong professional headshot uses clear direction, flattering light, a simple composition, and retouching that keeps you recognizable.</p><p>Plan the image around where it will appear: LinkedIn, a team page, press, casting, or a campaign. <a href="https://jordan-licon-photography.bloom.io/Professional-Headshot">Book a headshot session</a> or <a href="https://jordan-licon-photography.bloom.io/discovery">start a consultation</a> when you know the intended use.</p>';
    var contents=document.createElement('nav');
    contents.className='article-contents';
    contents.setAttribute('aria-label','Guide contents');
    contents.innerHTML='<h2>In this guide</h2><ol><li><a href="#what-is-a-professional-headshot">What makes a professional headshot?</a></li><li><a href="#five-elements">The five elements of a strong headshot</a></li><li><a href="#choose-photographer">How to choose a photographer</a></li><li><a href="#session">What to expect during the session</a></li><li><a href="#cost">Costs and final image choices</a></li></ol>';
    var checklist=document.createElement('section');
    checklist.className='article-checklist';
    checklist.setAttribute('aria-labelledby','checklist-title');
    checklist.innerHTML='<h2 id="checklist-title">Before you book</h2><ul><li>Decide where the image will appear: LinkedIn, a team page, press, casting, or a campaign.</li><li>Bring two or three wardrobe options that support your role and intended audience.</li><li>Ask about final crops, retouching, delivery timing, and licensing before the session.</li></ul>';
    trust.insertAdjacentElement('afterend',answer);
    answer.insertAdjacentElement('afterend',contents);
    contents.insertAdjacentElement('afterend',checklist);
  }
  function addScrollTracking(){
    var sent={50:false,75:false,90:false};
    window.addEventListener('scroll',function(){
      var max=document.documentElement.scrollHeight-window.innerHeight;
      if(max<=0)return;
      var depth=Math.round((window.scrollY/max)*100);
      [50,75,90].forEach(function(mark){if(depth>=mark&&!sent[mark]){sent[mark]=true;pushEvent('jlp_scroll_depth',{percent_scrolled:mark});}});
    },{passive:true});
  }
  document.addEventListener('DOMContentLoaded',function(){initMobileMenu();addHomepagePath();addTopServiceCards();addArticleGuide();addScrollTracking();});
})();
