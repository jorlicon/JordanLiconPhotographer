const slides = Array.from(document.querySelectorAll('#gallery .work img')).map((img, i) => ({display: img.getAttribute('src'), original: img.getAttribute('src').replace('/display/', '/'), alt: img.alt, label: `Food Portfolio ${String(i + 1).padStart(2, '0')}`}));
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  const caption = document.getElementById('lightbox-caption');
  let activeIndex = 0;
  function show(index) {
    activeIndex = (index + slides.length) % slides.length;
    const slide = slides[activeIndex];
    lightboxImg.src = slide.original;
    lightboxImg.alt = slide.alt;
    caption.textContent = slide.label;
    lightbox.classList.add('open');
  }
  document.querySelectorAll('.work').forEach((card) => card.addEventListener('click', () => show(Number(card.dataset.index))));
  document.querySelector('.lb-close').addEventListener('click', () => lightbox.classList.remove('open'));
  document.querySelector('.lb-prev').addEventListener('click', () => show(activeIndex - 1));
  document.querySelector('.lb-next').addEventListener('click', () => show(activeIndex + 1));
  lightbox.addEventListener('click', (event) => { if (event.target === lightbox) lightbox.classList.remove('open'); });
  document.addEventListener('keydown', (event) => {
    if (!lightbox.classList.contains('open')) return;
    if (event.key === 'Escape') lightbox.classList.remove('open');
    if (event.key === 'ArrowLeft') show(activeIndex - 1);
    if (event.key === 'ArrowRight') show(activeIndex + 1);
  });
