document.addEventListener("DOMContentLoaded", () => {
    const hamburgerButton = document.querySelector(".navbar-burger");
    const navMenu = document.querySelector(".navbar-menu");

    hamburgerButton.addEventListener("click", () => {
      hamburgerButton.classList.toggle("is-active");
      navMenu.classList.toggle("is-active");
    });

    const allDropdowns = document.querySelectorAll(
      ".navbar-item.has-dropdown"
    );

    allDropdowns.forEach((dropdown) => {
      dropdown.addEventListener("click", () => {
        const elem = dropdown.querySelector(".navbar-dropdown");
        elem.classList.toggle("is-active");
      });
    });
  });