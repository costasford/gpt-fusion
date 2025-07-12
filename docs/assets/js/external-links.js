document.addEventListener('DOMContentLoaded', () => {
  const anchors = document.querySelectorAll('a[href]');
  anchors.forEach(a => {
    const url = new URL(a.getAttribute('href'), window.location.href);
    if (url.host && url.host !== window.location.host) {
      a.setAttribute('target', '_blank');
      if (!a.getAttribute('rel')) {
        a.setAttribute('rel', 'noopener');
      }
    }
  });
});
