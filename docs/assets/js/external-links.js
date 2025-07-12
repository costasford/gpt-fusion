document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('a[href]').forEach((a) => {
    if (!a.getAttribute('target')) {
      a.setAttribute('target', '_blank');
    }
    const rel = a.getAttribute('rel');
    if (!rel || !rel.includes('noopener')) {
      a.setAttribute('rel', (rel ? rel + ' ' : '') + 'noopener');
    }
  });
});
