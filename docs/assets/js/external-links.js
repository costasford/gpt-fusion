document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('a[href]').forEach((a) => {
    if (!a.getAttribute('target')) {
      a.setAttribute('target', '_blank');
    }
    const rel = a.getAttribute('rel');
    if (!rel || !rel.includes('noopener')) {
      a.setAttribute('rel', (rel ? rel + ' ' : '') + 'noopener');
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
