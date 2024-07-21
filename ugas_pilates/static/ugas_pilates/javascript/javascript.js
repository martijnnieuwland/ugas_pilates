document.addEventListener('DOMContentLoaded', function () {

const navbar = document.querySelector('.navbar-custom');

window.addEventListener('scroll', function () {
  if (window.scrollY > 25) {
    // Change 50 to the scroll distance you want
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});
});
