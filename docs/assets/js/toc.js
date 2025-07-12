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
