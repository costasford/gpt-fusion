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
