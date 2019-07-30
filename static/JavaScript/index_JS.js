console.log("hey just started");
// ! Nav-Bar
const nacSlide = () => {
  const burger = document.querySelector(".burger");
  const nav = document.querySelector(".nav-links");
  const navlinks = document.querySelectorAll(".nav-links li");

  burger.addEventListener("click", () => {
    nav.classList.toggle("nav-active");

    navlinks.forEach((link, index) => {
      if (link.style.animation) {
        link.style.animation = "";
      } else {
        link.style.animation = `navlinksfade 0.5s ease forwards ${index / 7 +
          0.5}s`;
      }
    });

    burger.classList.toggle("toggle");
  });
};

nacSlide();

// ? Nav-Bar end

// ! click to qr page
const qrbtn = document.querySelector("#click-to-qr-btn");
