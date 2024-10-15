// Get the toggle buttons and the pop-up menus
const menuToggle = document.getElementById('menuToggle');
const popupMenu = document.getElementById('popupMenu');
const userIcon = document.getElementById('userIcon');
const userPopupMenu = document.getElementById('userPopupMenu');

// Toggle the hamburger pop-up menu
menuToggle.addEventListener('click', function() {
    popupMenu.classList.toggle('show');
});

// Toggle the user pop-up menu
userIcon.addEventListener('click', function() {
    userPopupMenu.classList.toggle('show');
});

// Close menus if clicked outside
document.addEventListener('click', function(event) {
    if (!menuToggle.contains(event.target) && !popupMenu.contains(event.target)) {
        popupMenu.classList.remove('show');
    }
    if (!userIcon.contains(event.target) && !userPopupMenu.contains(event.target)) {
        userPopupMenu.classList.remove('show');
    }
});
