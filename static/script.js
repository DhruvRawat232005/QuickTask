const toggle = document.getElementById('darkToggle');
const circleLabel = document.getElementById('circleLabel');

// Load saved mode
const darkMode = localStorage.getItem('darkMode') === 'true';
toggle.checked = darkMode;
document.body.classList.toggle('dark', darkMode);
circleLabel.textContent = darkMode ? 'D' : 'L';

// Toggle behavior
toggle.addEventListener('change', () => {
  const isDark = toggle.checked;
  document.body.classList.toggle('dark', isDark);
  localStorage.setItem('darkMode', isDark);
  circleLabel.textContent = isDark ? 'D' : 'L';
});
