// Interactive demos embedded on the homepage (formerly demo.html).
// Loaded as a classic (non-module) script so these functions are reachable
// from the onclick= attributes in index.md's raw HTML.

function processText(operation) {
  const input = document.getElementById('text-input').value;
  const output = document.getElementById('text-output');
  const codeElement = document.getElementById('text-code');

  let result = '';
  let code = '';

  // Matches gpt_fusion.word_count()'s handling of empty/whitespace-only
  // input: 0 words, not 1 (a bare .split(/\s+/) on an empty string
  // returns [""], length 1).
  const wordCount = input.trim() === '' ? 0 : input.trim().split(/\s+/).length;

  switch (operation) {
    case 'word_count':
      result = `Word Count: ${wordCount}`;
      code = `import gpt_fusion

text = "${input}"
count = gpt_fusion.word_count(text)
print(f"Word Count: {count}")  # ${wordCount}`;
      break;

    case 'reverse_words': {
      const reversed = input.trim().split(/\s+/).reverse().join(' ');
      result = `Reversed: "${reversed}"`;
      code = `import gpt_fusion

text = "${input}"
reversed_text = gpt_fusion.reverse_words(text)
print(f"Reversed: {reversed_text}")  # "${reversed}"`;
      break;
    }

    case 'palindrome': {
      const cleaned = input.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
      const isPalindrome = cleaned === cleaned.split('').reverse().join('');
      result = `Is Palindrome: ${isPalindrome}`;
      code = `import gpt_fusion

text = "${input}"
is_palindrome = gpt_fusion.is_palindrome(text)
print(f"Is Palindrome: {is_palindrome}")  # ${isPalindrome}`;
      break;
    }
  }

  // textContent, not innerHTML: `result`/`code` embed the raw user input
  // verbatim (e.g. the reversed-words case) - injecting them via innerHTML
  // would execute any HTML/script pasted into the text box.
  output.textContent = result;
  codeElement.textContent = code;
}

function analyzeCSV(operation) {
  const input = document.getElementById('csv-input').value;
  const output = document.getElementById('csv-output');

  output.classList.remove('text-red-300');

  const lines = input.trim().split('\n');
  if (lines.length < 2 || lines[0].toLowerCase() !== 'value') {
    output.classList.add('text-red-300');
    output.textContent = 'Error: CSV must have "value" header and numeric data';
    return;
  }

  const values = lines.slice(1).map((line) => parseFloat(line.trim())).filter((n) => !isNaN(n));

  if (values.length === 0) {
    output.classList.add('text-red-300');
    output.textContent = 'Error: No valid numeric values found';
    return;
  }

  let result = '';

  switch (operation) {
    case 'average': {
      const avg = values.reduce((a, b) => a + b, 0) / values.length;
      result = `Average: ${avg.toFixed(2)}`;
      break;
    }

    case 'median': {
      const sorted = [...values].sort((a, b) => a - b);
      const median =
        sorted.length % 2 === 0
          ? (sorted[sorted.length / 2 - 1] + sorted[sorted.length / 2]) / 2
          : sorted[Math.floor(sorted.length / 2)];
      result = `Median: ${median.toFixed(2)}`;
      break;
    }

    case 'stats': {
      const avg2 = values.reduce((a, b) => a + b, 0) / values.length;
      const sorted2 = [...values].sort((a, b) => a - b);
      const median2 =
        sorted2.length % 2 === 0
          ? (sorted2[sorted2.length / 2 - 1] + sorted2[sorted2.length / 2]) / 2
          : sorted2[Math.floor(sorted2.length / 2)];
      const min = Math.min(...values);
      const max = Math.max(...values);

      result = `📊 Full Statistics:
Count: ${values.length}
Average: ${avg2.toFixed(2)}
Median: ${median2.toFixed(2)}
Min: ${min.toFixed(2)}
Max: ${max.toFixed(2)}
Range: ${(max - min).toFixed(2)}`;
      break;
    }
  }

  output.textContent = result;
}

function showProjectCode(type) {
  const output = document.getElementById('project-output');

  let command = '';
  let description = '';

  switch (type) {
    case 'csv':
      command = 'gpt-fusion create_csv_app my-analytics --with-api';
      description = '📊 Creates a FastAPI backend with CSV processing and data visualization';
      break;
    case 'ui':
      command = 'gpt-fusion create_tailwind_ui my-webapp --dark-mode';
      description = '🎨 Generates a modern responsive UI with Tailwind CSS and dark mode';
      break;
    case 'fullstack':
      command = 'gpt-fusion create_fullstack_app my-saas --auth --database';
      description = '🚀 Complete application with authentication, database, and deployment ready';
      break;
  }

  // Fixed values only (no user input reaches this template), so innerHTML
  // is safe here - unlike processText/analyzeCSV above.
  output.innerHTML = `<div class="mb-2">${description}</div><div class="text-yellow-300 font-mono">${command}</div>`;
}
