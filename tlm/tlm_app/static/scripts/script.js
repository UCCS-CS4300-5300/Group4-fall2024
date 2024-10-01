// Get the toggle buttons and the pop-up menus
const menuToggle = document.getElementById('menuToggle');
const popupMenu = document.getElementById('popupMenu');
const userIcon = document.getElementById('userIcon');
const userPopupMenu = document.getElementById('userPopupMenu');

// Get the link buttons from the pop-ups
const aboutPageRedirect = document.getElementById('about-page-redirect')
const listPageRedirect = document.getElementById('list-page-redirect')
const loginPageRedirect = document.getElementById('login-page-redirect')
const profilePageRedirect = document.getElementById('profile-page-redirect')
const qTranslatePageRedirect = document.getElementById('qTranslate-page-redirect')
const settingsPageRedirect = document.getElementById('settings-page-redirect')

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

// Redirects from the index page to respective pages
aboutPageRedirect.addEventListener('click', function(event) {
    window.location.href = "about"
});

listPageRedirect.addEventListener('click', function(event) {
    window.location.href = "lists"
});

loginPageRedirect.addEventListener('click', function(event) {
    window.location.href = "login"
});

profilePageRedirect.addEventListener('click', function(event) {
    window.location.href = "profile"
});

qTranslatePageRedirect.addEventListener('click', function(event) {
    window.location.href = "quick_Translate"
});

settingsPageRedirect.addEventListener('click', function(event) {
    window.location.href = "settings"
});