  document.getElementById('year').textContent = new Date().getFullYear();

  // Hero 3D stack — mouse parallax tilt
  (function(){
    const stage = document.getElementById('stackStage');
    const stack = document.getElementById('stack3d');
    if(!stage || !stack) return;
    const baseX = 52, baseZ = -38;
    stage.addEventListener('mousemove', (e)=>{
      const r = stage.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width - 0.5;
      const py = (e.clientY - r.top) / r.height - 0.5;
      stack.style.transform = `rotateX(${baseX - py*22}deg) rotateZ(${baseZ + px*26}deg)`;
    });
    stage.addEventListener('mouseleave', ()=>{
      stack.style.transform = `rotateX(${baseX}deg) rotateZ(${baseZ}deg)`;
    });
  })();

  // Project card media — subtle tilt on hover
  document.querySelectorAll('[data-tilt]').forEach(card=>{
    const inner = card.querySelector('[data-tilt-inner]');
    card.addEventListener('mousemove', (e)=>{
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width - 0.5;
      const py = (e.clientY - r.top) / r.height - 0.5;
      inner.style.transform = `rotateY(${px*10}deg) rotateX(${-py*10}deg) translateZ(10px)`;
    });
    card.addEventListener('mouseleave', ()=>{
      inner.style.transform = `rotateY(0deg) rotateX(0deg) translateZ(0)`;
    });
  });
