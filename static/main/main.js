const toggleButton = document.querySelector('.threedots');
const myDiv = document.getElementById('dropdown');

toggleButton.addEventListener('click', () => {
    if (myDiv.classList.contains('hidden')) {
        myDiv.classList.remove('hidden');
    } else {
        myDiv.style.display = 'none';
    }
});