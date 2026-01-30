// Toggle mobile navigation menu
document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });

    // Accessibility: toggle on Enter key
    hamburger.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.keyCode === 13) {
            navLinks.classList.toggle('active');
        }
    });
});