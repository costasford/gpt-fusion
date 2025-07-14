document.addEventListener('DOMContentLoaded', () => {
  const button = document.getElementById('greet-btn');
  const output = document.getElementById('greet-output');
  if (!button || !output) return;

  button.addEventListener('click', async () => {
    const input = document.getElementById('name-input');
    const name = input ? input.value.trim() || 'Fusion' : 'Fusion';
    const apiBase = window.API_BASE || 'https://gpt-fusion-demo.fly.dev';
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
