document.addEventListener('DOMContentLoaded', function() {
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    const themeIcon = document.getElementById('themeIcon');
    const html = document.documentElement;

    const currentTheme = localStorage.getItem('theme') || 'dark';
    html.setAttribute('data-bs-theme', currentTheme);

    if (currentTheme === 'dark') {
        themeIcon.classList.add('fa-moon');
        themeIcon.classList.remove('fa-sun');
    } else {
        themeIcon.classList.add('fa-sun');
        themeIcon.classList.remove('fa-moon');
    }

    themeToggleBtn.addEventListener('click', function() {
        const newTheme = html.getAttribute('data-bs-theme') === 'dark' ? 'light' : 'dark';
        html.setAttribute('data-bs-theme', newTheme);
        localStorage.setItem('theme', newTheme);

        if (newTheme === 'dark') {
            themeIcon.classList.add('fa-moon');
            themeIcon.classList.remove('fa-sun');
        } else {
            themeIcon.classList.add('fa-sun');
            themeIcon.classList.remove('fa-moon');
        }
    });
});
