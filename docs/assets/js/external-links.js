document.addEventListener('DOMContentLoaded', () => {
  const anchors = document.querySelectorAll('a[href]');

  anchors.forEach((a) => {
    const url = new URL(a.getAttribute('href'), window.location.href);

    if (url.origin !== window.location.origin) {
      if (!a.hasAttribute('target')) {
        a.setAttribute('target', '_blank');
      }

      const rel = a.getAttribute('rel') || '';
      if (!rel.includes('noopener')) {
        a.setAttribute('rel', rel ? `${rel} noopener` : 'noopener');
      }
    }
  });
});
