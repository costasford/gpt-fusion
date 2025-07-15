// GENERATED: Combined utilities for docs pages
// GitHub Pages serves files over HTTP/2 so multiple requests are multiplexed,
// but bundling keeps asset counts low.

// external-links.js
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

// anchor-links.js
document.addEventListener('DOMContentLoaded', () => {
  const headings = document.querySelectorAll('h2, h3, h4, h5, h6');
  headings.forEach((h) => {
    if (!h.id) {
      const slug = h.textContent
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-|-$/g, '');
      h.id = slug;
    }

    const link = document.createElement('a');
    link.className = 'anchor-link';
    link.href = `#${h.id}`;
    link.textContent = '🔗';
    h.appendChild(link);
  });
});

// toc.js
document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('toc');
  if (!container) return;

  const headings = document.querySelectorAll('h2, h3');
  if (!headings.length) return;

  const list = document.createElement('ul');
  container.appendChild(list);

  headings.forEach((h) => {
    if (!h.id) {
      const slug = h.textContent
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-|-$/g, '');
      h.id = slug;
    }
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = `#${h.id}`;
    a.textContent = h.textContent;
    li.appendChild(a);
    list.appendChild(li);
  });
});
document.addEventListener('DOMContentLoaded', () => {
  const button = document.getElementById('greet-btn');
  const output = document.getElementById('greet-output');
  if (!button || !output) return;

  button.addEventListener('click', async () => {
    const input = document.getElementById('name-input');
    const name = input ? input.value.trim() || 'Fusion' : 'Fusion';
    const apiBase = window.API_BASE || '/api';
    try {
      const res = await fetch(`${apiBase}/greet/${encodeURIComponent(name)}`);
      if (!res.ok) throw new Error('Request failed');
      const data = await res.json();
      output.textContent = data.message;
    } catch {
      output.textContent = 'Request failed';
    }
  });
});
