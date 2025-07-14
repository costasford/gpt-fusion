// Toggle navigation menu
const navToggle = document.getElementById('nav-toggle');
const navMenu = document.getElementById('nav-menu');

function toggleMenu() {
    const expanded = navToggle.getAttribute('aria-expanded') === 'true';
    navToggle.setAttribute('aria-expanded', String(!expanded));
    navMenu.setAttribute('aria-expanded', String(!expanded));
}

navToggle.addEventListener('click', toggleMenu);

// Smooth scroll for anchor links
const links = document.querySelectorAll('a[href^="#"]');
links.forEach(link => {
    link.addEventListener('click', event => {
        const targetId = link.getAttribute('href').substring(1);
        const target = document.getElementById(targetId);
        if (target) {
            event.preventDefault();
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});
