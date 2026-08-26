function organizePortraitPortfolio(){
  const grid=document.getElementById('portfolio-grid');
  if(!grid||grid.dataset.organized)return;
  const works=Array.from(grid.querySelectorAll(':scope > .work'));
  const categories=[
    {id:'cat-fashion',label:'Fashion Editorial',deck:'Wardrobe-led portraits, fashion styling, cinematic scene work, and editorial portrait photography for publication, campaign, and personal-brand use.',items:[0,1,2,6,7,8,9,12,13,14,15,16,17]},
    {id:'cat-beauty',label:'Beauty + Glamour',deck:'Polished beauty portraits, controlled studio light, elevated styling, and images built around face, gesture, and refined presence.',items:[21,22,23,24,31,32]},
    {id:'cat-actor',label:'Actor + Character Portraits',deck:'Character-driven editorial portraits with stronger narrative, mood, and identity; useful for performers, artists, and creative professionals.',items:[3,4,10,11,33,34]},
    {id:'cat-pageantry',label:'Pageantry + Performance',deck:'Gown, crown, stage, and performance-adjacent portraiture with a polished finish for pageant, musician, and public-facing talent use.',items:[18,19,20,45,35,36,39,40]},
    {id:'cat-studio',label:'Studio Portraits',deck:'Controlled-light portrait sessions with a cleaner studio read, strong color, wardrobe variety, and commercial personal-brand utility.',items:[5,27,28,29,30,37,38,41,42]},
    {id:'cat-men',label:"Men's Editorial Portraits",deck:'Masculine editorial portraits and actor-branding images shaped around expression, wardrobe, props, and cinematic character.',items:[25,26,43,44]}
  ];
  const byIndex=new Map(works.map(work=>[Number(work.dataset.index),work]));
  grid.className='portfolio-categories';
  grid.innerHTML='';
  categories.forEach((category,categoryIndex)=>{
    const section=document.createElement('section');
    section.className='category-section';
    section.id=category.id;
    section.innerHTML=`<div class="category-title"><div class="mono">${String(categoryIndex+1).padStart(2,'0')} / ${category.items.length} images</div><div><h3>${category.label}</h3><p>${category.deck}</p></div></div><div class="grid"></div>`;
    const sectionGrid=section.querySelector('.grid');
    category.items.forEach(index=>{
      const work=byIndex.get(index);
      if(work)sectionGrid.appendChild(work);
    });
    grid.appendChild(section);
  });
  grid.dataset.organized='true';
}
organizePortraitPortfolio();
const images=Array.from(document.querySelectorAll('.work img')).map(img=>({src:img.getAttribute('src'),alt:img.alt}));let active=0;const box=document.getElementById('lightbox'),boxImg=box.querySelector('img');function show(i){active=i;let item=images[i];if(!item){const img=document.querySelector(`.work[data-index="${i}"] img`);item=img?{src:img.currentSrc||img.src,alt:img.alt}:images[((i%images.length)+images.length)%images.length]}boxImg.src=item.src;boxImg.alt=item.alt;box.classList.add('open')}document.querySelectorAll('.work').forEach(btn=>btn.addEventListener('click',()=>show(Number(btn.dataset.index))));box.querySelector('.close').addEventListener('click',()=>box.classList.remove('open'));box.querySelector('.prev').addEventListener('click',()=>show(active-1));box.querySelector('.next').addEventListener('click',()=>show(active+1));document.addEventListener('keydown',e=>{if(!box.classList.contains('open'))return;if(e.key==='Escape')box.classList.remove('open');if(e.key==='ArrowLeft')show(active-1);if(e.key==='ArrowRight')show(active+1)});
